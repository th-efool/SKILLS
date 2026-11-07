"""Discover, prepare, repair and mount an archived website in Next.js App Router."""
import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import urllib.request
from urllib.parse import urlsplit
import zipfile
from prepare import prepare, valid_media, MEDIA, within


def discover(archive, entry=None, origin=None):
    with zipfile.ZipFile(archive) as z:
        entries = [n for n in z.namelist() if n.lower().endswith(('index.html', 'index.htm')) and '__MACOSX' not in n]
        if entry:
            entries = [entry]
        entries.sort(key=lambda n: (len(Path(n).parts), n))
        if not entries:
            raise ValueError('Inspect ZIP for its homepage or buildable source project; supply an HTML --entry after building.')
        if len(entries) > 1 and len(Path(entries[0]).parts) == len(Path(entries[1]).parts):
            # Exported dependency/analytics hosts usually have no canonical homepage.
            canonical = [n for n in entries if re.search(r'<link[^>]+rel=["\']canonical', z.read(n).decode('utf-8', errors='replace'), re.I)]
            if len(canonical) == 1:
                entries = canonical
            else:
                raise ValueError('Choose --entry from these homepage candidates: ' + ', '.join(entries[:15]))
        entry = entries[0]
        text = z.read(entry).decode('utf-8', errors='replace')
    class Canonical(HTMLParser):
        url = None
        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == 'link' and attrs.get('rel', '').lower() == 'canonical':
                self.url = attrs.get('href')
    parser = Canonical()
    parser.feed(text)
    inferred = urlsplit(parser.url or '')
    if not origin and inferred.scheme in {'http', 'https'} and inferred.netloc:
        origin = inferred.scheme + '://' + inferred.netloc
    if not origin:
        hosts = [part for part in Path(entry).parts[:-1] if re.fullmatch(r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}', part)]
        if hosts: origin = 'https://' + hosts[0]
    if not origin:
        raise ValueError('Read site metadata and supply its confirmed --origin.')
    hostname = urlsplit(origin).hostname or ''
    parts = hostname.removeprefix('www.').split('.')
    common_second_level = {'co', 'com', 'org', 'net', 'gov', 'ac'}
    brand = parts[-3] if len(parts) >= 3 and parts[-2] in common_second_level and len(parts[-1]) == 2 else parts[-2] if len(parts) >= 2 else parts[0]
    return entry, origin, '/' + re.sub(r'[^a-z0-9-]', '-', brand.lower())


def parse_js(node, code, kind='module'):
    return subprocess.run([node, '--input-type=' + kind, '--check'], input=code, text=True, capture_output=True, encoding='utf-8')


def repair_operators(node, code, kind='module'):
    """Change only a split operator touching Node's current syntax-error caret."""
    original = code
    for _ in range(300):
        result = parse_js(node, code, kind)
        if result.returncode == 0: return code, None
        lines = result.stderr.splitlines()
        location = next((i for i, s in enumerate(lines) if re.match(r'^\[stdin\]:\d+$', s)), None)
        if location is None or location + 2 >= len(lines): break
        number = int(lines[location].split(':')[-1]) - 1
        caret = lines[location + 2].find('^')
        source_lines = code.splitlines(keepends=True)
        if number >= len(source_lines): break
        offset = sum(len(s) for s in source_lines[:number])
        line = source_lines[number]
        # Export beautifiers can insert a forbidden newline after async.
        if 'Unexpected reserved word' in result.stderr and number > 0:
            previous = source_lines[number - 1]
            if re.search(r'\basync[ \t]*\r?\n$', previous) and re.match(r'\s*function\b', line):
                start = offset - len(previous)
                code = code[:start] + previous.rstrip() + ' ' + line.lstrip() + code[offset + len(line):]
                continue
        candidates = list(re.finditer(r'\?\s+\.|\?\s+\?\s*=?|\?\?\s+=|\|\|\s+=|&&\s+=', line))
        candidate = next((m for m in candidates if m.start() <= caret <= m.end()), None)
        # Node omits its caret for extremely long source lines. A unique
        # split-operator candidate can still be tested, with full rollback.
        if caret < 0 and len(candidates) == 1:
            candidate = candidates[0]
        if candidate is None: break
        start, end = offset + candidate.start(), offset + candidate.end()
        replacement = re.sub(r'\s+', '', candidate[0])
        code = code[:start] + replacement + code[end:]
    # Apply all proposed repairs together only when the complete script parses.
    return original, result.stderr[:1600]


def repair_scripts(served, actions, findings):
    node = shutil.which('node')
    if not node:
        findings.append('Node required for JavaScript syntax checks and repair')
        return
    for file in served.rglob('*'):
        if file.suffix.lower() not in {'.html', '.htm', '.js', '.mjs'}: continue
        try: text = file.read_text(encoding='utf-8-sig')
        except UnicodeDecodeError: continue
        def fix(code, label, kind='module'):
            fixed, error = repair_operators(node, code, kind)
            if error: findings.append({'script': label, 'error': error})
            if fixed != code: actions.append({'repaired_script': label, 'method': 'Parser-located export damage; complete syntax check passed'})
            return fixed
        if file.suffix.lower() in {'.js', '.mjs'}:
            updated = fix(text, str(file))
        else:
            def inline(match):
                attrs, code = match[1], match[2]
                kind = re.search(r'\btype\s*=\s*["\']([^"\']+)', attrs, re.I)
                kind = kind[1].lower() if kind else 'text/javascript'
                if not code.strip() or kind not in {'module', 'text/javascript', 'application/javascript'}: return match[0]
                return '<script' + attrs + '>' + fix(code, str(file) + ' inline', 'module' if kind == 'module' else 'commonjs') + '</script>'
            updated = re.sub(r'<script\b([^>]*)>(.*?)</script\s*>', inline, text, flags=re.S | re.I)
        if updated != text: file.write_text(updated, encoding='utf-8')


def recover(url, target):
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 WebsiteArchiveImport'})
    with urllib.request.urlopen(request, timeout=30) as response:
        # Limit automatic recovery to ordinary individual assets.
        data = response.read(100_000_001)
        content_type = response.headers.get_content_type()
    if len(data) > 100_000_000 or content_type == 'text/html':
        raise ValueError('Recovery returned oversized asset or HTML')
    staging = target.with_name(target.name + '.download')
    staging.parent.mkdir(parents=True, exist_ok=True)
    staging.write_bytes(data)
    try:
        # Signature validator uses the real extension.
        probe = target.with_name('recovery-probe-' + target.name)
        if probe.exists(): raise FileExistsError(probe)
        staging.rename(probe)
        try:
            if target.suffix.lower() in MEDIA and not valid_media(probe):
                raise ValueError('Recovered media signature is invalid')
            probe.replace(target)
        finally:
            if probe.exists(): probe.unlink()
    finally:
        if staging.exists(): staging.unlink()


def run(args):
    if args.report:
        report_path = Path(args.report).resolve()
        report = json.loads(report_path.read_text(encoding='utf-8'))
    else:
        entry, origin, default_route = discover(args.zip, args.entry, args.origin)
        report_path, report = prepare(args.zip, args.project, entry, args.route or default_route, origin)
    served = Path(report['served_directory']).resolve()
    project = Path(args.project).resolve()
    if not served.is_relative_to(project / 'public' / 'website-imports'):
        raise ValueError('Report serving directory must belong to this project')
    actions, findings = [], []
    root_relative = report['root_asset_prefix'].removeprefix('/website-imports/' + served.name).lstrip('/')
    root = within(served, root_relative)
    recoveries = {str(within(root, item['path'].lstrip('/'))): item['recovery_url'] for item in report['missing_root_assets']}
    for rel in report['invalid_media_signatures']:
        file = within(served, rel)
        if file.is_relative_to(root):
            recoveries[str(file)] = report['origin'] + '/' + file.relative_to(root).as_posix()
        else:
            findings.append({'invalid_external_media': rel, 'next': 'Use the archived host folder and reference URL to recover or retain valid external URL'})
    for name, url in recoveries.items():
        target = Path(name)
        if target.is_file() and target.suffix.lower() in MEDIA and valid_media(target): continue
        try:
            recover(url, target)
            actions.append({'recovered': str(target), 'url': url})
        except Exception as error:
            findings.append({'asset': name, 'url': url, 'error': str(error)})
    repair_scripts(served, actions, findings)
    for file in served.rglob('*.html'):
        text = file.read_text(encoding='utf-8-sig')
        def nav(match):
            attrs, path, tail = match[1], match[2], match[3]
            if path.startswith(('/website-imports/', '//')): return match[0]
            if path == '/':
                href = report['served_entry']
                return '<a' + attrs + 'href="' + href + '"' + tail + '>'
            if Path(urlsplit(path).path).suffix.lower() in MEDIA | {'.svg', '.css', '.js', '.ico'}: return match[0]
            # Each absent original subpage has an explicit safe destination.
            rest = re.sub(r'\s+(?:target|rel)\s*=\s*(?:"[^"]*"|\x27[^\x27]*\x27)', '', attrs + tail, flags=re.I)
            return '<a' + rest + ' href="' + html.escape(report['origin'] + path, quote=True) + '" target="_blank" rel="noopener noreferrer">'
        updated = re.sub(r'<a\b([^>]*?)href="(/[^"#]*)"([^>]*)>', nav, text, flags=re.I)
        if updated != text: file.write_text(updated, encoding='utf-8')
    app = project / 'src' / 'app' if (project / 'src' / 'app').is_dir() else project / 'app'
    if not app.is_dir():
        findings.append('Inspect framework and mount served_entry in its router; Next.js app directory was not found')
    else:
        route_dir = within(app, report['route'].lstrip('/'))
        existing = next((route_dir / n for n in ('page.tsx', 'page.jsx', 'page.js', 'page.ts') if (route_dir / n).exists()), None)
        marker = '// Generated by idiot-website-stealer\n'
        content = existing.read_text(encoding='utf-8') if existing else ''
        placeholder = bool(re.fullmatch(r'\s*export default function \w+\(\)\s*\{\s*return\s*<main>[^<>]*</main>;?\s*\}\s*', content))
        if existing and not (args.replace_page or placeholder or content.startswith(marker)):
            findings.append({'route_collision': str(existing), 'next': 'Inspect existing content; use --replace-page when user requested replacement'})
        else:
            target = existing or route_dir / 'page.tsx'
            if existing and not content.startswith(marker):
                backup = report_path.parent / ('original-' + target.name)
                if not backup.exists(): shutil.copy2(target, backup)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(marker + 'export default function ImportedWebsite() {\n  return <iframe src=' + json.dumps(report['served_entry']) + ' title=' + json.dumps('Website: ' + urlsplit(report['origin']).hostname) + ' style={{ border: 0, position: "fixed", inset: 0, width: "100%", height: "100dvh", background: "white" }} />;\n}\n', encoding='utf-8')
            actions.append({'mounted_route': report['route'], 'file': str(target)})
    result = {'route': report['route'], 'served_entry': report['served_entry'], 'report': str(report_path),
              'actions': actions, 'remaining_findings': findings,
              'next': 'Resolve findings, update index if applicable, run build, start/reuse server, complete browser-acceptance.md and save screenshots.'}
    output = report_path.parent / 'import-result.json'
    output.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({'result_file': str(output), **result}, indent=2))
    return result


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    group = cli.add_mutually_exclusive_group(required=True)
    group.add_argument('--zip')
    group.add_argument('--report')
    cli.add_argument('--project', required=True)
    cli.add_argument('--route')
    cli.add_argument('--entry')
    cli.add_argument('--origin')
    cli.add_argument('--replace-page', action='store_true')
    run(cli.parse_args())
