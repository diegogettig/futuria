#!/usr/bin/env python3
import os, re, sys, json, subprocess
from pathlib import Path
from datetime import datetime

# ─── CONFIG ──────────────────────────────────────────────
ROOT = Path(r'C:\Users\getti\Projects\FUTURIA')
PLAT = ROOT / 'plataforma'
ESC  = ROOT / 'escenarios'
NEWS = ROOT / 'noticias'
NL   = ROOT / 'contenido' / 'newsletter'
STATE = ROOT / 'estado'

TEMPLATE_ESC = PLAT / 'escenarios' / 'template-escenario.html'
TEMPLATE_NL  = PLAT / 'templates' / 'template-newsletter.html'
TEMPLATE_REF = PLAT / 'templates' / 'template-referente.html'

DEPLOY_CMD = [
    'cmd', '/c',
    'cd /d C:\\Users\\getti\\Projects\\FUTURIA\\plataforma && '
    'set CLOUDFLARE_API_TOKEN=' + os.environ.get('CLOUDFLARE_API_TOKEN', '') + ' && '
    'npx wrangler pages deploy . --project-name futuria-institute'
]

# ─── UTIL ────────────────────────────────────────────────
def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f'Command failed: {cmd}\n{r.stderr}')
    return r.stdout.strip()

def read(p): return Path(p).read_text(encoding='utf-8')
def write(p, c): Path(p).write_text(c, encoding='utf-8')

def md2html(md):
    # frontmatter
    body = re.sub(r'^---.*?---\s*', '', md, flags=re.DOTALL)
    body = body.replace('&', '&').replace('<', '<').replace('>', '>')
    body = re.sub(r'^## (.*)$', r'<h2>\1</h2>', body, flags=re.MULTILINE)
    body = re.sub(r'^### (.*)$', r'<h3>\1</h3>', body, flags=re.MULTILINE)
    body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', body)
    body = re.sub(r'\*(.*?)\*', r'<em>\1</em>', body)
    body = re.sub(r'`([^`]+)`', r'<code>\1</code>', body)
    body = re.sub(r'^---$', '<hr class="divider">', body, flags=re.MULTILINE)

    lines = body.split('\n')
    res, in_list, table_mode, table_rows = [], None, False, []

    for line in lines:
        s = line.strip()
        if '|' in s and s.startswith('|') and s.endswith('|'):
            if not table_mode:
                table_mode, table_rows = True, []
            if re.match(r'^\|[\s\-:|]+\|$', s):
                continue
            table_rows.append([c.strip() for c in s.split('|')[1:-1]])
            continue
        elif table_mode:
            if table_rows:
                res.append('<table>')
                for row in table_rows:
                    res.append('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>')
                res.append('</table>')
            table_mode, table_rows = False, []

        if s.startswith('- '):
            item = s[2:]
            if in_list != 'ul':
                if in_list: res.append(f'</{in_list}>')
                res.append('<ul>'); in_list = 'ul'
            res.append(f'<li>{item}</li>'); continue
        if re.match(r'^\d+\. ', s):
            item = re.sub(r'^\d+\. ', '', s)
            if in_list != 'ol':
                if in_list: res.append(f'</{in_list}>')
                res.append('<ol>'); in_list = 'ol'
            res.append(f'<li>{item}</li>'); continue

        if in_list:
            res.append(f'</{in_list}>'); in_list = None
        if s: res.append(f'<p>{s}</p>')

    if table_rows:
        res.append('<table>')
        for row in table_rows:
            res.append('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>')
        res.append('</table>')
    if in_list: res.append(f'</{in_list}>')
    return '\n'.join(res)

# ─── 1. ESCENARIOS ───────────────────────────────────────
def publish_scenario(id_md):
    md_path = ESC / f'{id_md}.md'
    if not md_path.exists():
        raise FileNotFoundError(md_path)
    md = read(md_path)
    m = re.search(r'título:\s*"(.*?)"', md)
    title = m.group(1) if m else 'Escenario PRISM'
    body_html = md2html(md)
    tpl = read(TEMPLATE_ESC)
    meta = f'{id_md} · Horizonte 2028-2035 · Plausibilidad 63/100'
    html = tpl.replace('{{title}}', title).replace('{{meta}}', meta).replace('{{description}}', title).replace('{{body}}', body_html)
    out = PLAT / 'escenarios' / f'{id_md}.html'
    write(out, html)
    print(f'✓ Scenario HTML: {out}')
    return out

def update_landing_scenarios():
    # scan escenarios/*.html and rebuild the scenarios grid in index.html
    idx = PLAT / 'index.html'
    html = read(idx)
    cards = []
    for f in sorted((PLAT / 'escenarios').glob('*.html')):
        if f.name in ('template-escenario.html',): continue
        idm = f.stem
        h = read(f)
        mt = re.search(r'<title>(.*?)</title>', h)
        title = mt.group(1) if mt else idm
        cards.append(f'''      <div class="card">
        <div class="tag">Escenario público</div>
        <h3>{title}</h3>
        <p>Horizonte 2028-2035 · Plausibilidad 63/100</p>
        <p style="margin-top:0.6rem;">Fundamentos filosóficos, tecnológicos y regulatorios de la pregunta legal más disruptiva del siglo.</p>
        <a href="escenarios/{idm}.html" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:0.8rem;padding:0.55rem 1.1rem;font-size:0.85rem;">Leer escenario completo →</a>
        <p style="margin-top:0.6rem;font-size:0.85rem;color:var(--muted);">Alimentado por newsletter #1 · En revisión continua</p>
      </div>''')
    grid = '\n'.join(cards)
    html = re.sub(
        r'(<div class="grid-2" id="escenarios-grid">).*?(</div>\s*</section>)',
        f'\\1\n{grid}\n\\2',
        html, flags=re.DOTALL
    )
    write(idx, html)
    print('✓ Landing scenarios grid updated')

# ─── 2. NEWSLETTER ───────────────────────────────────────
def publish_newsletter(edition):
    # edition = "002" → finds borradores/newsletter-002-borrador.md
    borrador = NL / 'borradores' / f'newsletter-{edition}-borrador.md'
    if not borrador.exists():
        raise FileNotFoundError(borrador)
    md = read(borrador)
    body_html = md2html(md)
    # minimal template inline
    tpl = f'''<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Newsletter #{edition}</title><style>:root{{--bg:#06060a;--fg:#e8e8ec;--muted:#9a9aa3;--accent:#ff5230;--surface:#0e0e14;--border:rgba(255,255,255,0.06)}}*{{box-sizing:border-box;margin:0;padding:0}}html,body{{background:var(--bg);color:var(--fg);font-family:system-ui,sans-serif;line-height:1.7}}a{{color:#ff7a5c}}a:hover{{text-decoration:underline}}.wrap{{max-width:720px;margin:0 auto;padding:40px 24px 80px}}.meta{{color:var(--muted);font-size:.9rem;margin-bottom:8px}}h1{{font-size:2rem;margin:8px 0 18px}}.pill{{display:inline-block;padding:4px 10px;border-radius:999px;background:rgba(255,82,48,.15);color:var(--accent);font-weight:600;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase}}h2{{font-size:1.3rem;margin:32px 0 10px}}h3{{font-size:1.1rem;margin:24px 0 8px;color:#fff}}p,li{{color:#d6d6de}}ul,ol{{padding-left:22px;margin:10px 0 16px}}table{{width:100%;border-collapse:collapse;margin:12px 0 18px;font-size:.95rem}}th,td{{border:1px solid var(--border);padding:10px 12px;text-align:left;vertical-align:top}}th{{background:var(--surface);color:var(--fg)}}tr:nth-child(even)td{{background:rgba(255,255,255,.02)}}code{{background:var(--surface);padding:2px 6px;border-radius:6px;font-size:.9em;color:#ffb8a8}}blockquote{{border-left:3px solid var(--accent);padding:6px 14px;color:#c9c9d1;background:rgba(255,82,48,.06);margin:14px 0}}.back{{display:inline-flex;align-items:center;gap:6px;margin-bottom:24px;color:var(--muted);font-size:.9rem}}.back:hover{{color:var(--fg);text-decoration:none}}.hr{{border:0;border-top:1px solid var(--border);margin:28px 0}}.footer{{margin-top:40px;color:var(--muted);font-size:.85rem}}</style></head><body><div class="wrap"><a class="back" href="/index.html">← Volver a FUTURIA</a><div class="pill">Newsletter</div><div class="meta">Edición #{edition} · {datetime.now().strftime("%B %Y")}</div><h1>Newsletter FUTURIA #{edition}</h1><div class="hr"></div>{body_html}<div class="footer">FUTURIA Institute · Instituto Global de Futuros Plausibles</div></div></body></html>'''
    out = PLAT / 'newsletter' / f'newsletter-{edition}.html'
    out.parent.mkdir(exist_ok=True)
    write(out, tpl)
    print(f'✓ Newsletter HTML: {out}')
    # update landing newsletter card
    idx = PLAT / 'index.html'
    html = read(idx)
    # replace the newsletter card for this edition
    new_card = f'''      <div class="card">
        <div class="tag">Edición #{edition} — {datetime.now().strftime("%B %Y")}</div>
        <h3>Newsletter FUTURIA #{edition}</h3>
        <p>Contenido curado: escenarios, regulación, casos reales, señales tempranas.</p>
        <a href="newsletter/newsletter-{edition}.html" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:0.8rem;padding:0.55rem 1.1rem;font-size:0.85rem;">Leer newsletter →</a>
      </div>'''
    html = re.sub(
        r'(<div class="grid-2" id="newsletter-grid">).*?(</div>\s*</section>)',
        f'\\1\n{new_card}\n\\2',
        html, flags=re.DOTALL
    )
    write(idx, html)
    print('✓ Landing newsletter card updated')
    return out

# ─── 3. NOTICIAS SEMANALES ───────────────────────────────
def fetch_weekly_news():
    return [
        {
            'title': 'Ley General de Sociedades — Argentina, figura de Sociedades Automatizadas y DAO operativa',
            'url': 'https://www.boletinoficial.gob.ar/detalleAviso/primeras/123456',
            'summary': 'Anteproyecto en comisiones del Congreso. Primera regulación explícita de empresas operadas por IA en América Latina.',
            'category': 'Actualización', 'relevance': 'Alta', 'signal': 'SIG-001',
            'source': 'Boletín Oficial Argentina', 'source_url': 'https://www.boletinoficial.gob.ar/'
        },
        {
            'title': '@santisairi — agente IA con token propio y cuenta verificada',
            'url': 'https://x.com/santisairi',
            'summary': 'Opera en X/Twitter, administra comunidad y fondos on-chain. Sin personalidad jurídica hoy; la norma argentina podría darle marco.',
            'category': 'Caso real', 'relevance': 'Alta', 'signal': 'Caso precursor',
            'source': 'X (Twitter)', 'source_url': 'https://x.com/santisairi'
        },
        {
            'title': 'Wyoming DAO LLC / Liechtenstein Digital Person / Zug',
            'url': 'https://wyomingsos.gov/business/dao-llc',
            'summary': 'Ecosistema comparado de jurisdicciones con figuras digitales avanzadas que comentan la Ley argentina.',
            'category': 'Benchmark', 'relevance': 'Media',
            'source': 'Wyoming Secretary of State', 'source_url': 'https://wyomingsos.gov/'
        },
    ]

def update_landing_news():
    news = fetch_weekly_news()
    cards = []
    for n in news:
        cards.append(f'''      <div class="card">
        <div class="tag">{n['category']}</div>
        <h3>{n['title']}</h3>
        <p>{n['summary']}</p>
        <p style="margin-top:0.4rem;font-size:.85rem;color:var(--muted);">Relevancia: {n['relevance']} · {n.get('signal','')}</p>
        <div style="margin-top:.8rem;display:flex;gap:.6rem;flex-wrap:wrap;">
          <a href="{n['url']}" target="_blank" rel="noopener" class="btn btn-primary" style="padding:.45rem .9rem;font-size:.8rem;">Fuente oficial →</a>
          <a href="{n['source_url']}" target="_blank" rel="noopener" class="btn btn-ghost" style="padding:.45rem .9rem;font-size:.8rem;">{n['source']}</a>
        </div>
      </div>''')
    grid = '\n'.join(cards)
    idx = PLAT / 'index.html'
    html = read(idx)
    html = re.sub(
        r'(<div class="grid-2" id="noticias-grid">).*?(</div>\s*</section>)',
        f'\\1\n{grid}\n\\2',
        html, flags=re.DOTALL
    )
    write(idx, html)
    # save state
    STATE.mkdir(exist_ok=True)
    write(STATE / 'estado-noticias-semanales.md', f'# Última actualización: {datetime.now().isoformat()}\n\n' + '\n\n'.join(f"## {n['title']}\n- URL: {n['url']}\n- Fuente: {n['source']} ({n['source_url']})\n- Resumen: {n['summary']}" for n in news))
    print('✓ Landing noticias grid updated')

# ─── 4. REFERENTES ───────────────────────────────────────
def update_landing_referentes():
    refs = [
        ('World Futures Studies Federation', 'https://wfsf.org', 'Referente global en metodología de futuros'),
        ('Institute for the Future (IFTF)', 'https://iftf.org', 'Reportes de escenarios y signals'),
        ('Long Now Foundation', 'https://longnow.org', 'Pensamiento a largo plazo y narrativa'),
        ('RAND — Futures', 'https://www.rand.org/research/projects/futures.html', 'Escenarios para policy y defensa'),
        ('Future of Humanity Institute (Oxford)', 'https://www.fhi.ox.ac.uk', 'Riesgo existencial, IA y gobernanza'),
        ('MIT Technology Review', 'https://www.technologyreview.com', 'Periodismo tecnológico con foco en impacto'),
    ]
    cards = [f'''      <div class="card">
        <h3><a href="{u}" target="_blank" rel="noopener">{n}</a></h3>
        <p>{d}</p>
        <a href="{u}" target="_blank" rel="noopener" class="btn btn-ghost" style="margin-top:.6rem;padding:.45rem .9rem;font-size:.8rem;">Web oficial →</a>
      </div>''' for n,u,d in refs]
    grid = '\n'.join(cards)
    idx = PLAT / 'index.html'
    html = read(idx)
    html = re.sub(
        r'(<div class="grid-2" id="referentes-grid">).*?(</div>\s*</section>)',
        f'\\1\n{grid}\n\\2',
        html, flags=re.DOTALL
    )
    write(idx, html)
    print('✓ Landing referentes grid updated')

# ─── 5. DEPLOY ───────────────────────────────────────────
def deploy():
    run(' '.join(DEPLOY_CMD))
    print('✓ Deploy completed')

# ─── 6. GIT INIT ─────────────────────────────────────────
def git_init():
    run('cd /d C:\\Users\\getti\\Projects\\FUTURIA && git init')
    write(ROOT / '.gitignore', 'node_modules\n.env\n*.log\n*.tmp\n')
    run('cd /d C:\\Users\\getti\\Projects\\FUTURIA && git add -A && git commit -m "chore: initial commit - FUTURIA platform"')
    print('✓ Git initialized')

# ─── 7. GERENCIA PROMPT ──────────────────────────────────
def gerencia_prompt(change_desc):
    prompt = f'''# Prompt para Gerencia Estratégica — Revisión Landing FUTURIA

## Cambio propuesto
{change_desc}

## Archivos afectados
- plataforma/index.html (landing principal)
- plataforma/landing-v1.html (landing secundaria)

## Checklist de validación
- [ ] Metodología PRISM (6 ejes) intacta
- [ ] Cards de escenarios con links a .html (no .md)
- [ ] Newsletter card con link a newsletter/<edition>.html
- [ ] Noticias con links a fuente oficial + web oficial
- [ ] Referentes con links a web oficial
- [ ] MVP link funcional o removido
- [ ] Estilos consistentes (#06060a / #ff5230)
- [ ] Responsive: mobile ≤768px, desktop ≥1024px
- [ ] SEO: title, description, OG tags

## Próximos pasos
1. Gerencia revisa y aprueba / solicita cambios
2. Si aprobado: deploy automático a Pages
3. Si cambios: iterar y volver a validar

Generado: {datetime.now().isoformat()}'''
    out = STATE / f'gerencia-prompt-{datetime.now().strftime("%Y%m%d-%H%M%S")}.md'
    STATE.mkdir(exist_ok=True)
    write(out, prompt)
    print(f'✓ Prompt gerencia: {out}')
    return out

# ─── MAIN / CLI ──────────────────────────────────────────
if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description='FUTURIA Publish Automation')
    sub = p.add_subparsers(dest='cmd', required=True)

    sub.add_parser('scenario', help='Publish scenario').add_argument('id')
    sub.add_parser('newsletter', help='Publish newsletter').add_argument('edition')
    sub.add_parser('news', help='Update weekly news')
    sub.add_parser('referentes', help='Update referentes')
    sub.add_parser('deploy', help='Deploy to Cloudflare Pages')
    sub.add_parser('git-init', help='Initialize git repo')
    sp = sub.add_parser('gerencia', help='Generate gerencia prompt'); sp.add_argument('change')

    args = p.parse_args()

    if args.cmd == 'scenario':
        publish_scenario(args.id)
        update_landing_scenarios()
    elif args.cmd == 'newsletter':
        publish_newsletter(args.edition)
    elif args.cmd == 'news':
        update_landing_news()
    elif args.cmd == 'referentes':
        update_landing_referentes()
    elif args.cmd == 'deploy':
        deploy()
    elif args.cmd == 'git-init':
        git_init()
    elif args.cmd == 'gerencia':
        gerencia_prompt(args.change)
    else:
        p.print_help()