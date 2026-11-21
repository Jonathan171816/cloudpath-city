#!/usr/bin/env python3
"""Une CSS, HTML y JS en un solo archivo. Salidas: dist/index.html (GitHub Pages) y dist/artifact.html (fragmento para Claude)."""
import pathlib
root = pathlib.Path(__file__).parent
src = root / 'src'
css = (src / 'style.css').read_text(encoding='utf-8')
body = (src / 'body.html').read_text(encoding='utf-8')
order = ['data-az900.js', 'data-az104.js', 'data-az305.js', 'labs.js', 'incidents.js', 'engine.js']
js = '\n'.join((src / f).read_text(encoding='utf-8') for f in order)
fonts = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap" rel="stylesheet">'
title = '<title>CloudPath City</title>'
sheet = '<div class="sheet" id="sheet" hidden role="dialog" aria-modal="true" tabindex="-1"><div class="sheet-in" id="sheetIn"></div></div>'
core = f'<style>\n{css}\n</style>\n{body}\n<script>\n{js}\n</script>'
(root / 'dist').mkdir(exist_ok=True)
full = f'<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n{title}\n<meta name="description" content="Aprende Azure construyendo una ciudad: AZ-900, AZ-104 y AZ-305 con estudio, retos y laboratorios simulados.">\n{fonts}\n</head>\n<body>\n{core}\n</body>\n</html>\n'
(root / 'dist' / 'index.html').write_text(full, encoding='utf-8')
frag = f'{title}\n<meta name="claude:viewport-fit-sides" content="cover">\n{fonts}\n{core}\n'
(root / 'dist' / 'artifact.html').write_text(frag, encoding='utf-8')
print('index.html', len(full), 'bytes; artifact.html', len(frag), 'bytes')
