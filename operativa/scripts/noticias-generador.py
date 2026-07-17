#!/usr/bin/env python3
"""FUTURIA — Generador operativo de noticias relevantes."""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
NEWS_FILE = BASE / "operativa" / "noticias.json"
HTML_FILE = BASE / "plataforma" / "noticias.html"


def load_news():
    if NEWS_FILE.exists():
        return json.loads(NEWS_FILE.read_text(encoding="utf-8"))
    return {"ultima_actualizacion": None, "noticias": []}


def save_news(data):
    NEWS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def seed_if_empty():
    data = load_news()
    if data["noticias"]:
        return data

    data["ultima_actualizacion"] = datetime.now(timezone.utc).isoformat()
    data["noticias"] = [
        {
            "id": "n-001",
            "titulo": "CronJob de vigilancia tecnológica listo",
            "fuente": "FUTURIA",
            "fecha": datetime.now(timezone.utc).isoformat(),
            "relevancia": "Estructura operativa publicada en noticias.html.",
            "ejes": ["operativa"]
        }
    ]
    save_news(data)
    return data


def build_html(data):
    items = ""
    for n in data["noticias"]:
        fecha = n.get("fecha", "")[:10]
        items += f"""<div class="item">
  <div class="meta">{fecha} · {n.get('fuente', '')} · {', '.join(n.get('ejes', []))}</div>
  <h3>{n.get('titulo', '')}</h3>
  <p style="color:var(--muted);">{n.get('relevancia', '')}</p>
</div>
"""
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FUTURIA — Noticias</title>
  <style>
    :root {{ --bg:#06060a; --text:#e4e4ec; --muted:#8a8a9e; --accent:#ff5230; --border:rgba(255,255,255,0.07); --card:rgba(255,255,255,0.03); }}
    *, *::before, *::after {{ box-sizing:border-box; margin:0; padding:0; }}
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; background:var(--bg); color:var(--text); line-height:1.75; }}
    a {{ color: var(--accent); text-decoration: none; }}
    .container {{ max-width: 1180px; margin: 0 auto; padding: 0 1.8rem; }}
    nav {{ position: fixed; top: 0; left: 0; right: 0; z-index: 50; background: rgba(6,6,10,0.85); backdrop-filter: blur(14px); border-bottom: 1px solid var(--border); }}
    .nav-inner {{ max-width: 1180px; margin: 0 auto; padding: 1rem 1.8rem; display: flex; align-items: center; justify-content: space-between; }}
    .nav-brand {{ font-weight: 900; letter-spacing: -0.04em; font-size: 1.3rem; color: #fff; text-decoration:none; }}
    .nav-brand em {{ color: var(--accent); font-style: normal; }}
    .back {{ color: var(--muted); font-size: 0.9rem; margin-top: 3.2rem; display: inline-block; }}
    .section-title {{ font-size: 2.1rem; font-weight: 800; margin-top: 3.2rem; letter-spacing: -0.03em; }}
    .section-title em {{ color: var(--accent); font-style: normal; }}
    .section-lead {{ color: var(--muted); font-size: 1.1rem; max-width: 760px; margin-top: 0.6rem; margin-bottom: 2rem; }}
    .item {{ border-bottom: 1px solid var(--border); padding: 1.2rem 0; }}
    .item h3 {{ color: #fff; font-size: 1.1rem; }}
    .meta {{ color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.3rem; }}
  </style>
</head>
<body>
<nav>
  <div class="nav-inner">
    <a href="/" class="nav-brand">FUTU<em>RIA</em></a>
    <a href="/" class="back">← Volver al sitio</a>
  </div>
</nav>

<div class="container">
  <div class="section-title">Noticias <em>por fecha</em></div>
  <p class="section-lead">Cobertura curada cada 2 días desde vigilancia automatizada. Fuentes oficiales, papers y señales tempranas.</p>
{items}
  <p style="color:var(--muted);font-size:0.9rem;margin-top:2rem;">Última actualización: {data.get('ultima_actualizacion','—')}</p>
</div>

</body>
</html>
"""
    HTML_FILE.write_text(html, encoding="utf-8")


def add_noticia(titulo, fuente, relevancia, ejes):
    data = load_news()
    nid = f"n-{len(data['noticias'])+1:03d}"
    data["noticias"].append({
        "id": nid,
        "titulo": titulo,
        "fuente": fuente,
        "fecha": datetime.now(timezone.utc).isoformat(),
        "relevancia": relevancia,
        "ejes": ejes,
    })
    data["ultima_actualizacion"] = datetime.now(timezone.utc).isoformat()
    save_news(data)
    build_html(data)
    return nid


def main():
    seed_if_empty()
    data = load_news()
    build_html(data)
    print(json.dumps({"actualizadas": len(data["noticias"]), "ultima": data["ultima_actualizacion"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
