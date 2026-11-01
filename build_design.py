"""Inline the Galmuri11 font into the Design Ring spin-off and write design-ring.html."""
import base64, pathlib
here = pathlib.Path(__file__).parent
dist = here / "node_modules" / "galmuri" / "dist"
enc = lambda f: base64.b64encode((dist / f).read_bytes()).decode()
src = (here / "design-ring.src.html").read_text(encoding="utf-8")
out = src.replace("__FONT_REG__", enc("Galmuri11.woff2")).replace("__FONT_BOLD__", enc("Galmuri11-Bold.woff2"))
(here / "design-ring.html").write_text(out, encoding="utf-8")
print("wrote design-ring.html")
