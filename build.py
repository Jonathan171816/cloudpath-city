#!/usr/bin/env python3
"""Build the self-contained game with Python's standard library. No CDN is used."""
from pathlib import Path
import base64
import re
from html import escape

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'src'
ORDER = ['data-az900.js', 'data-az104.js', 'data-az305.js', 'labs.js',
         'incidents.js', 'world.js', 'engine.js']


def build():
    fonts = []
    for family, filename in [('Press Start 2P', 'PressStart2P'), ('VT323', 'VT323')]:
        path = ROOT / 'assets' / 'fonts' / (filename + '.woff2')
        if not path.exists():
            path = path.with_suffix('.ttf')
        encoded = base64.b64encode(path.read_bytes()).decode('ascii')
        extension = path.suffix[1:]
        fmt = 'woff2' if extension == 'woff2' else 'truetype'
        fonts.append("@font-face{font-family:'%s';font-style:normal;font-weight:400;"
                     "font-display:swap;src:url(data:font/%s;base64,%s) format('%s');}" %
                     (family, extension, encoded, fmt))
    css = '\n'.join(fonts) + '\n' + (SRC / 'style.css').read_text(encoding='utf-8')
    body = (SRC / 'body.html').read_text(encoding='utf-8')
    notices = '\n\n'.join((ROOT / 'assets' / 'fonts' / name).read_text(encoding='utf-8')
                           for name in ['PressStart2P-OFL.txt', 'VT323-OFL.txt'])
    notices = '\n'.join(line.rstrip() for line in notices.splitlines())
    body += '\n<template id="bundled-font-licenses"><pre>' + escape(notices) + '</pre></template>'
    js = '\n\n'.join('// Source: ' + name + '\n' + (SRC / name).read_text(encoding='utf-8') for name in ORDER)
    js = re.sub(r'</script', r'<\\/script', js, flags=re.I)
    html = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#101a2c">
<meta name="description" content="CloudPath City: una aventura Azure con Nimbus. Casos originales, laboratorios y retos expertos para AZ-900, AZ-104 y AZ-305.">
<meta name="cloudpath-version" content="3.0-nimbus">
<title>CloudPath City · Expedición Nimbus</title>
<style>''' + css + '''</style>
</head>
<body>
''' + body + '\n<script>\n' + js + '\n</script>\n</body>\n</html>\n'
    (ROOT / 'dist').mkdir(exist_ok=True)
    for path in [ROOT / 'index.html', ROOT / 'dist' / 'index.html']:
        path.write_text(html, encoding='utf-8')
    (ROOT / 'dist' / '.nojekyll').write_text('')
    print(f'Built index.html and dist/index.html: {len(html.encode("utf-8")):,} bytes; no network dependencies.')


if __name__ == '__main__':
    build()
