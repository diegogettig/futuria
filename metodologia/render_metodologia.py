"""render_metodologia.py — Genera la pÃ¡gina HTML propia de la MetodologÃ­a de
Plausibilidad del Instituto FUTURIA a partir de metodologia/plausibilidad-metodologia.md.

Uso:
    python render_metodologia.py

Produce: metodologia/plausibilidad-metodologia.html
El markdown se convierte a HTML con un mini-parser (sin dependencias externas)
conservando el estilo visual de los escenarios PRISM.
"""
import pathlib, re, html

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "plausibilidad-metodologia.md"
OUT = ROOT / "plausibilidad-metodologia.html"

# ---------- mini markdown -> html ----------
def md_inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)          # negrita
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)          # codigo
    s = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', s)  # links
    return s

def md_to_html(md):
    lines = md.splitlines()
    out, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        if ln.startswith("### "):
            out.append(f'<h3>{md_inline(ln[4:])}</h3>')
        elif ln.startswith("## "):
            out.append(f'<h2 class="sec">{md_inline(ln[3:])}</h2>')
        elif ln.startswith("# "):
            out.append(f'<h1>{md_inline(ln[2:])}</h1>')
        elif ln.startswith("| "):
            # tabla (procesa el bloque completo)
            tbl = []
            while i < n and lines[i].startswith("|"):
                tbl.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            # descartar fila separadora --- | --- 
            rows = [r for r in tbl if not all(set(c) <= set("-: ") for c in r)]
            head, *body = rows
            t = ['<table class="mtable"><thead><tr>' + "".join(f"<th>{md_inline(h)}</th>" for h in head) + "</tr></thead><tbody>"]
            for r in body:
                t.append("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue
        elif ln.startswith("- "):
            items = []
            while i < n and lines[i].startswith("- "):
                items.append(f"<li>{md_inline(lines[i][2:])}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        elif ln.startswith("```"):
            i += 1
            code = []
            while i < n and not lines[i].startswith("```"):
                code.append(lines[i]); i += 1
            out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
        elif ln.strip() == "":
            pass
        else:
            out.append(f"<p>{md_inline(ln)}</p>")
        i += 1
    return "\n".join(out)

body = md_to_html(SRC.read_text(encoding="utf-8"))

HTML = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Metodología de Plausibilidad — Instituto FUTURIA</title>
<style>
:root{{--bg:#06060a;--card:#101018;--border:#23232f;--text:#d6d6e0;--muted:#8a8a9a;--accent:#7c5cff}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--text);font:16px/1.65 -apple-system,Segoe UI,Roboto,sans-serif}}
.nav{{position:sticky;top:0;background:rgba(6,6,10,.9);border-bottom:1px solid var(--border);padding:.8rem 1.4rem;z-index:5}}
.nav a{{color:var(--accent);text-decoration:none;font-weight:600}}
.wrap{{max-width:820px;margin:0 auto;padding:2.4rem 1.4rem 5rem}}
h1{{font-size:2rem;color:#fff;margin-bottom:.2rem}}
h2.sec{{color:#fff;margin-top:2.4rem;border-left:3px solid var(--accent);padding-left:.7rem}}
h3{{color:#fff;margin-top:1.6rem}}
p{{color:var(--text)}}
code{{background:var(--card);padding:.15rem .4rem;border-radius:.4rem;font-size:.9em;color:#b9a6ff}}
pre{{background:var(--card);border:1px solid var(--border);border-radius:.8rem;padding:1rem;overflow-x:auto}}
pre code{{background:none;padding:0;color:var(--text)}}
.mtable{{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.92rem}}
.mtable th,.mtable td{{border:1px solid var(--border);padding:.5rem .7rem;text-align:left;vertical-align:top}}
.mtable th{{background:var(--card);color:#fff}}
.mtable td code{{word-break:break-all}}
ul{{padding-left:1.2rem}}
li{{margin:.3rem 0}}
.badge{{display:inline-block;background:var(--card);border:1px solid var(--accent);color:var(--accent);border-radius:99px;padding:.2rem .8rem;font-size:.8rem;font-weight:600;margin-bottom:1rem}}
.note{{background:var(--card);border:1px solid var(--border);border-radius:.8rem;padding:1rem 1.2rem;margin:1.2rem 0;color:var(--muted);font-size:.9rem}}
</style>
</head>
<body>
<div class="nav"><a href="index.html">← Volver</a> · <a href="plausibilidad-metodologia.md">Ver markdown fuente ↗</a></div>
<div class="wrap">
<div class="badge">DOCUMENTO OFICIAL DEL INSTITUTO</div>
{body}
<div class="note">Este documento es la fuente canónica del criterio de plausibilidad de escenarios PRISM. Cualquier modificación requiere nuevo hash SHA-256, anclaje en blockchain y firma del revisor humano (ver §9).</div>
</div>
</body>
</html>'''

OUT.write_text(HTML, encoding="utf-8")
print("OK ->", OUT, len(HTML), "bytes")
