"""Inline the Galmuri11 pixel font, the sound clips (sounds/) and the English text (lang-en.txt) into the game
and write index.html (the only built file).
Run `npm install galmuri@2.39.3` in this folder first.

    python3 build.py                     -> index.html
    python3 build.py --artifact PATH     -> also an unwrapped copy at PATH, for publishing as a claude.ai artifact
"""
import base64, json, pathlib, sys
here = pathlib.Path(__file__).parent
dist = here / "node_modules" / "galmuri" / "dist"
src = (here / "agora-ring.src.html").read_text(encoding="utf-8")
enc = lambda f: base64.b64encode((dist / f).read_bytes()).decode()
out = src.replace("__FONT_REG__", enc("Galmuri11.woff2")).replace("__FONT_BOLD__", enc("Galmuri11-Bold.woff2"))
# Handjet for English (fonts/, SIL OFL: fonts/Handjet-OFL.txt)
hj = lambda f: base64.b64encode((here / "fonts" / f).read_bytes()).decode()
out = (out.replace("__FONT_HJ_LATIN__", hj("handjet-latin.woff2")).replace("__FONT_HJ_LATINEXT__", hj("handjet-latin-ext.woff2"))
          .replace("__FONT_HJ_GREEK__", hj("handjet-greek.woff2")))
# sound clips (sounds/ is kept out of git; see README)
snd = lambda f: base64.b64encode((here / "sounds" / f).read_bytes()).decode()
out = out.replace("__SND_PUNCH__", snd("punches.wav")).replace("__SND_BELL__", snd("bell.mp3"))
# English text: one "Korean ||| English" pair per line, '#' starts a comment line
en = {}
for ln in (here / "lang-en.txt").read_text(encoding="utf-8").splitlines():
    if ln.strip() and not ln.startswith("#"):
        ko, sep, e = ln.partition(" ||| ")
        if not sep: sys.exit(f"lang-en.txt: no ' ||| ' in {ln!r}")
        en[ko] = e
out = out.replace("/*__LANG_EN__*/{}", json.dumps(en, ensure_ascii=False).replace("</", "<\\/"))
if "--artifact" in sys.argv:
    # The artifact host adds its own document skeleton, so this copy stays unwrapped.
    path = pathlib.Path(sys.argv[sys.argv.index("--artifact") + 1])
    path.write_text(out, encoding="utf-8")
    print(f"wrote {path}")
# The source is an artifact fragment (no doctype/charset); wrap it so the file also opens standalone.
if not out.lstrip().lower().startswith("<!doctype"):
    out = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           '<style>body{margin:0}</style></head><body>\n' + out + '\n</body></html>')
(here / "index.html").write_text(out, encoding="utf-8")
print("wrote index.html")
