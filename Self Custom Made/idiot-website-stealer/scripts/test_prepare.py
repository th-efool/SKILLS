import tempfile
import unittest
import zipfile
from pathlib import Path
from prepare import prepare, extract


class ImportTests(unittest.TestCase):
    def test_scoped_assets_and_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / 'site.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('example.com/index.html', '<link href="/_astro/site.css"><img src="/assets/missing.png"><a href="/pricing">Pricing</a><script>let x = y ? .z;</script>')
                z.writestr('example.com/_astro/site.css', 'body{background:url(/assets/missing.png)}')
                z.writestr('example.com/_astro/broken.js', 'let x; x || = 1;')
                z.writestr('example.com/assets/hero.mp4', b'not a video')
            _, report = prepare(archive, root / 'app', 'example.com/index.html', '/pageX', 'https://example.com')
            original = Path(report['source']) / 'example.com/index.html'
            served = Path(report['served_directory']) / 'example.com/index.html'
            self.assertIn('href="/_astro/site.css"', original.read_text())
            self.assertIn(report['root_asset_prefix'] + '/_astro/site.css', served.read_text())
            self.assertIn('href="/pricing"', served.read_text())
            self.assertEqual(report['missing_root_assets'][0]['recovery_url'], 'https://example.com/assets/missing.png')
            self.assertIn('example.com/assets/hero.mp4', report['invalid_media_signatures'])
            if report['javascript_parser'].endswith(('node', 'node.exe')):
                self.assertEqual(len(report['script_parse_errors']), 2)
            with self.assertRaises(FileExistsError):
                prepare(archive, root / 'app', 'example.com/index.html', '/pageX', 'https://example.com')

    def test_rejects_traversal_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / 'bad.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('index.html', 'valid entry')
                z.writestr('../escaped.txt', 'escape')
            with self.assertRaises(ValueError):
                extract(archive, root / 'extracted')
            self.assertFalse((root / 'extracted/index.html').exists())
            self.assertFalse((root / 'escaped.txt').exists())


if __name__ == '__main__':
    unittest.main()
