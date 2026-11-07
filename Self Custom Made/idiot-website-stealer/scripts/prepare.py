"""Prepare an isolated static website import; emit evidence for subsequent repair."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import zipfile
from urllib.parse import unquote, urlsplit


TEXT = {'.html', '.htm', '.css', '.js', '.mjs', '.json', '.svg'}
MEDIA = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.woff', '.woff2', '.mp4'}
ROOT_REF = re.compile(r'''(?P<lead>["'`(=])(?P<path>/(?!/)[^\s"'`<>)]*)''')


def within(root, relative):
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f'Path leaves destination: {relative}')
    return target


def extract(archive, destination):
    with zipfile.ZipFile(archive) as bundle:
        entries = bundle.infolist()
        if len(entries) > 100000 or sum(e.file_size for e in entries) > 2_000_000_000:
            raise ValueError('Archive exceeds the preparation limit; inspect before expanding limits.')
        seen = set()
        for entry in entries:
            name = entry.filename.replace('\\', '/')
            parts = PurePosixPath(name).parts
            if name.startswith('/') or any(p in {'..', '.'} or ':' in p for p in parts):
                raise ValueError(f'Unsafe archive entry: {name}')
            if stat.S_ISLNK(entry.external_attr >> 16):
                raise ValueError(f'Symlink requires inspection: {name}')
            key = name.rstrip('/').casefold()
            if key in seen:
                raise ValueError(f'Duplicate archive path: {name}')
            seen.add(key)
            within(destination, name)
        for entry in entries:
            target = within(destination, entry.filename.replace('\\', '/'))
            if entry.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with bundle.open(entry) as src, target.open('wb') as dst:
                    shutil.copyfileobj(src, dst)


def valid_media(path):
    with path.open('rb') as stream:
        b = stream.read(32)
    ext = path.suffix.lower()
    if ext == '.png': return b.startswith(b'\x89PNG\r\n\x1a\n')
    if ext in {'.jpg', '.jpeg'}: return b.startswith(b'\xff\xd8\xff')
    if ext == '.gif': return b.startswith((b'GIF87a', b'GIF89a'))
    if ext == '.webp': return b.startswith(b'RIFF') and b[8:12] == b'WEBP'
    if ext == '.woff': return b.startswith(b'wOFF')
    if ext == '.woff2': return b.startswith(b'wOF2')
    if ext == '.mp4': return b[4:8] in {b'ftyp', b'styp', b'moov', b'mdat'}
    return True


def prepare(archive, project, entry, route, origin):
    archive, project = Path(archive).resolve(), Path(project).resolve()
    if not re.fullmatch(r'/[A-Za-z0-9_-]+(?:/[A-Za-z0-9_-]+)*', route):
        raise ValueError('Choose an explicit route such as /LandingPageA or /antigravity.')
    parsed = urlsplit(origin)
    if parsed.scheme not in {'http', 'https'} or not parsed.netloc or parsed.path not in {'', '/'} or parsed.query or parsed.fragment:
        raise ValueError('Origin must be a confirmed HTTP(S) origin, e.g. https://antigravity.google')
    origin = origin.rstrip('/')
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()[:10]
    slug = route.strip('/').replace('/', '-').lower()
    key = f'{slug}-{digest}'
    work = project / '.website-imports' / key
    served = project / 'public' / 'website-imports' / key
    if work.exists() or served.exists():
        raise FileExistsError(f'Import already exists; inspect/reuse its report: {work / "report.json"}')
    source = work / 'source'
    # Validate entry and archive paths before extracting any payload.
    entry_path = within(source, entry)
    extract(archive, source)
    if not entry_path.is_file() or entry_path.suffix.lower() not in {'.html', '.htm'}:
        raise ValueError(f'Choose an existing HTML entry from the extraction: {entry}')
    root = entry_path.parent
    prefix = '/website-imports/' + key
    root_prefix = prefix + '/' + root.relative_to(source).as_posix().strip('.')
    root_prefix = root_prefix.rstrip('/')
    shutil.copytree(source, served)
    asset_dirs = {'_astro', '_next', 'assets', 'static', 'images', 'img', 'fonts', 'css', 'js', 'media', 'videos'}
    missing, changed, invalid, parse_errors = set(), [], [], []
    node = shutil.which('node')
    for original in source.rglob('*'):
        if not original.is_file(): continue
        rel = original.relative_to(source)
        dest = served / rel
        if original.suffix.lower() in MEDIA and not valid_media(original):
            invalid.append(rel.as_posix())
        if original.suffix.lower() not in TEXT: continue
        try:
            text = original.read_text(encoding='utf-8-sig')
        except UnicodeDecodeError:
            changed.append({'file': rel.as_posix(), 'finding': 'Non-UTF8 text: inspect charset before rewriting'})
            continue
        def rewrite(match):
            path = match['path']
            url_path = unquote(urlsplit(path).path)
            try:
                local = within(root, url_path.lstrip('/'))
            except ValueError:
                return match[0]
            first = url_path.lstrip('/').split('/')[0]
            is_asset = first in asset_dirs or Path(url_path).suffix.lower() in MEDIA | {'.css', '.js', '.mjs', '.svg', '.ico'}
            if is_asset:
                if not local.is_file(): missing.add(url_path)
                return match['lead'] + root_prefix + path
            return match[0]
        updated = ROOT_REF.sub(rewrite, text)
        if updated != text:
            dest.write_text(updated, encoding='utf-8')
            changed.append({'file': rel.as_posix(), 'finding': 'Scoped root asset references'})
        scripts = []
        if original.suffix.lower() in {'.js', '.mjs'}:
            scripts.append((rel.as_posix(), updated, 'module'))
        if original.suffix.lower() in {'.html', '.htm'}:
            for i, match in enumerate(re.finditer(r'<script\b([^>]*)>(.*?)</script\s*>', updated, re.S | re.I)):
                attrs, code = match.groups()
                kind = re.search(r'\btype\s*=\s*["\']([^"\']+)', attrs, re.I)
                kind = kind[1].lower() if kind else 'text/javascript'
                if code.strip() and kind in {'module', 'text/javascript', 'application/javascript'}:
                    scripts.append((f'{rel.as_posix()} inline script {i + 1}', code, 'module' if kind == 'module' else 'commonjs'))
        if node:
            for label, code, kind in scripts:
                result = subprocess.run([node, '--input-type=' + kind, '--check'], input=code, text=True, capture_output=True, encoding='utf-8')
                if result.returncode:
                    parse_errors.append({'file': label, 'error': result.stderr[:1800]})
    report = {
        'route': route, 'origin': origin, 'source': str(source), 'served_directory': str(served),
        'served_entry': prefix + '/' + entry_path.relative_to(source).as_posix(),
        'root_asset_prefix': root_prefix, 'changes': changed,
        'missing_root_assets': [{'path': p, 'recovery_url': origin + p} for p in sorted(missing)],
        'invalid_media_signatures': invalid, 'script_parse_errors': parse_errors,
        'javascript_parser': node or 'Unavailable: run syntax checks when Node is available',
        'next_step': 'Repair findings, mount route, build, then verify settled desktop/mobile rendering and interactions in browser.',
    }
    report_path = work / 'report.json'
    report_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    return report_path, report


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    for name in ('zip', 'project', 'entry', 'route', 'origin'):
        cli.add_argument('--' + name, required=True)
    args = cli.parse_args()
    report_path, report = prepare(args.zip, args.project, args.entry, args.route, args.origin)
    print(json.dumps({'report': str(report_path), 'route': report['route'], 'served_entry': report['served_entry'],
                      'missing': len(report['missing_root_assets']), 'invalid_media': len(report['invalid_media_signatures']),
                      'syntax_errors': len(report['script_parse_errors'])}, indent=2))
