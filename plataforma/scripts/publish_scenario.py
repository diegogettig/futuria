#!/usr/bin/env python3
import re, sys
from pathlib import Path

def esc(id, md_path, template_path, out_dir):
    md = Path(md_path).read_text(encoding='utf-8')
    tpl = Path(template_path).read_text(encoding='utf-8')
    out = Path(out_dir) / f'{id}.html'

    title = 'Escenario PRISM'
    m = re.search(r'título:\s*"(.*?)"', md)
    if m:
        title = m.group(1)

    body = re.sub(r'^---.*?---\s*', '', md, flags=re.DOTALL)
    body = body.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    body = re.sub(r'^## (.*)$', r'<h2>\1</h2>', body, flags=re.MULTILINE)
    body = re.sub(r'^### (.*)$', r'<h3>\1</h3>', body, flags=re.MULTILINE)
    body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', body)
    body = re.sub(r'\*(.*?)\*', r'<em>\1</em>', body)
    body = re.sub(r'`([^`]+)`', r'<code>\1</code>', body)
    body = re.sub(r'^---$', '<hr class="divider">', body, flags=re.MULTILINE)

    lines = body.split('\n')
    res = []
    in_list = None
    table_mode = False
    table_rows = []

    for line in lines:
        s = line.strip()
        if '|' in s and s.startswith('|') and s.endswith('|'):
            if not table_mode:
                table_mode = True
                table_rows = []
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
            table_mode = False
            table_rows = []

        if s.startswith('- '):
            item = s[2:]
            if in_list != 'ul':
                if in_list:
                    res.append(f'</{in_list}>')
                res.append('<ul>')
                in_list = 'ul'
            res.append(f'<li>{item}</li>')
            continue
        if re.match(r'^\d+\. ', s):
            item = re.sub(r'^\d+\. ', '', s)
            if in_list != 'ol':
                if in_list:
                    res.append(f'</{in_list}>')
                res.append('<ol>')
                in_list = 'ol'
            res.append(f'<li>{item}</li>')
            continue

        if in_list:
            res.append(f'</{in_list}>')
            in_list = None
        if s:
            res.append(f'<p>{s}</p>')

    if table_rows:
        res.append('<table>')
        for row in table_rows:
            res.append('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>')
        res.append('</table>')
    if in_list:
        res.append(f'</{in_list}>')

    body = '\n'.join(res)
    meta = f'{id} · Horizonte 2028-2035 · Plausibilidad 63/100'
    desc = title
    html = tpl.replace('{{title}}', title).replace('{{meta}}', meta).replace('{{description}}', desc).replace('{{body}}', body)
    out.write_text(html, encoding='utf-8')
    print(str(out))

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 4:
        print('usage: publish_scenario.py <id> <md_path> <template_path> <out_dir>')
        sys.exit(1)
    esc(*args)
