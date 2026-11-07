import argparse
import contextlib
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import zipfile
from import_site import discover, repair_operators, run


class RunnerTests(unittest.TestCase):
    def fixture(self, root):
        archive = root / 'example.zip'
        with zipfile.ZipFile(archive, 'w') as z:
            z.writestr('antigravity.google/index.html', '<link href="/_astro/site.css" rel="stylesheet"><link rel="canonical" href="https://antigravity.google/"><a href="/download">Download</a><a href="#features">Features</a><img src="/assets/test.png">')
            z.writestr('antigravity.google/_astro/site.css', 'body{color:black}')
            z.writestr('antigravity.google/_astro/script.js', 'let x = {}; x ? .a; x ? ? = 1;')
        return archive

    def test_default_route_recovery_mount_and_rerun(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = self.fixture(root)
            project = root / 'project'
            (project / 'app').mkdir(parents=True)
            args = argparse.Namespace(zip=str(archive), report=None, project=str(project), route=None, entry=None, origin=None, replace_page=False)
            def fake_recover(url, path):
                self.assertEqual(url, 'https://antigravity.google/assets/test.png')
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b'\x89PNG\r\n\x1a\n')
            with patch('import_site.recover', side_effect=fake_recover), contextlib.redirect_stdout(io.StringIO()):
                result = run(args)
            self.assertEqual(result['route'], '/antigravity')
            self.assertFalse(result['remaining_findings'])
            page = project / 'app/antigravity/page.tsx'
            self.assertIn(result['served_entry'], page.read_text())
            report = json.loads(Path(result['report']).read_text())
            index = Path(report['served_directory']) / 'antigravity.google/index.html'
            self.assertIn('https://antigravity.google/download', index.read_text())
            self.assertIn('href="#features"', index.read_text())
            args.report, args.zip = result['report'], None
            with patch('import_site.recover', side_effect=AssertionError('Valid recovered asset should be reused')), contextlib.redirect_stdout(io.StringIO()):
                second = run(args)
            self.assertFalse(second['remaining_findings'])

    def test_explicit_route_and_populated_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = self.fixture(root)
            project = root / 'project'
            page = project / 'app/pageX/page.tsx'
            page.parent.mkdir(parents=True)
            page.write_text('export default function Page() { return <main>Existing product</main>; }\n// preserve my work')
            before = page.read_bytes()
            args = argparse.Namespace(zip=str(archive), report=None, project=str(project), route='/pageX', entry=None, origin=None, replace_page=False)
            with patch('import_site.recover', side_effect=OSError('Unavailable')), contextlib.redirect_stdout(io.StringIO()):
                result = run(args)
            self.assertEqual(result['route'], '/pageX')
            self.assertEqual(page.read_bytes(), before)
            self.assertTrue(any('route_collision' in f for f in result['remaining_findings']))

    def test_parser_located_repairs_preserve_strings(self):
        node = shutil.which('node')
        if not node: self.skipTest('Node unavailable')
        code = 'const message = "literal ? . || ="; let x = {}; x ? .a; x ? ? = 1;'
        repaired, error = repair_operators(node, code)
        self.assertIsNone(error)
        self.assertIn('"literal ? . || ="', repaired)
        self.assertIn('x ?.a', repaired)
        self.assertIn('x ??= 1', repaired)
        async_code = 'async\nfunction load(){return await Promise.resolve(1)}'
        fixed_async, async_error = repair_operators(node, async_code)
        self.assertIsNone(async_error)
        self.assertIn('async function', fixed_async)
        long_code = 'let x={}; ' + 'x.a=1;' * 400 + 'x.a || = 2;'
        fixed_long, long_error = repair_operators(node, long_code)
        self.assertIsNone(long_error)
        self.assertIn('x.a ||= 2', fixed_long)
        unsupported = 'let = ;'
        repaired, error = repair_operators(node, unsupported)
        self.assertEqual(repaired, unsupported)
        self.assertIsNotNone(error)


if __name__ == '__main__':
    unittest.main()
