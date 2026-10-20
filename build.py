"""Inline the Galmuri11 pixel font into the game and write agora-ring.html.
Run `npm install galmuri@2.39.3` in this folder first."""
import base64, pathlib
here = pathlib.Path(__file__).parent
dist = here / "node_modules" / "galmuri" / "dist"
src = (here / "agora-ring.src.html").read_text(encoding="utf-8")
enc = lambda f: base64.b64encode((dist / f).read_bytes()).decode()
out = src.replace("__FONT_REG__", enc("Galmuri11.woff2")).replace("__FONT_BOLD__", enc("Galmuri11-Bold.woff2"))
# Unwrapped copy for publishing as a claude.ai artifact (the artifact host adds its own document skeleton).
(here / "agora-ring.artifact.html").write_text(out, encoding="utf-8")
# The source is an artifact fragment (no doctype/charset); wrap it so the file also opens standalone.
if not out.lstrip().lower().startswith("<!doctype"):
    out = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           '<style>body{margin:0}</style></head><body>\n' + out + '\n</body></html>')
(here / "agora-ring.html").write_text(out, encoding="utf-8")
(here / "index.html").write_text(out, encoding="utf-8")  # GitHub Pages entry point
print("wrote agora-ring.html, index.html")
