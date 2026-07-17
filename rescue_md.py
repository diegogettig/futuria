#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rescue_md.py — Rescata los .md fuente 0002-0009 leyendolos cuando el mount
MSYS los revele, y los vuelca a respaldo-escenarios/ (fuera del arbol inestable).
Reintenta hasta agotar ventanas. Correr en background.
"""
import os, time, glob, datetime

ROOT = os.getcwd()
DST = os.path.join(ROOT, "respaldo-escenarios")
os.makedirs(DST, exist_ok=True)

NUMS = ['0002','0003','0004','0005','0006','0007','0008','0009']
NAMES = {
 '0002':'sociedades-automatizadas','0003':'cardio-bionico','0004':'hard-tech-foundations',
 '0005':'gobernanza-algoritmica','0006':'longevidad-caas','0007':'conciencia-verificable',
 '0008':'bioprinting-distribuido','0009':'geopolitica-datos'}

log = open(os.path.join(ROOT,"rescue_md.log"),"a",encoding="utf-8")

def try_read(num):
    # 1) intentar glob para obtener nombre real
    pat = f"escenarios/PRISM-2026-{num}-*.md"
    for _ in range(40):
        try:
            fs = glob.glob(pat)
            if fs:
                src = fs[0]
                data = open(src, "rb").read()
                if data:
                    return data
        except Exception:
            pass
        time.sleep(0.5)
    # 2) fallback nombre canonico
    cand = f"escenarios/PRISM-2026-{num}-{NAMES[num]}.md"
    for _ in range(40):
        try:
            data = open(cand, "rb").read()
            if data:
                return data
        except Exception:
            pass
        time.sleep(0.5)
    return None

for attempt in range(1, 600):  # ~ hasta 10 min de reintentos globales
    t = datetime.datetime.now().strftime("%H:%M:%S")
    pending = [n for n in NUMS if not os.path.exists(os.path.join(DST, f"PRISM-2026-{n}-{NAMES[n]}.md"))]
    if not pending:
        log.write(f"{t} TODOS RESCATADOS\n"); break
    for num in pending:
        data = try_read(num)
        if data:
            out = os.path.join(DST, f"PRISM-2026-{num}-{NAMES[num]}.md")
            open(out, "wb").write(data)
            log.write(f"{t} RESCATADO {num} ({len(data)} bytes)\n")
    if attempt % 30 == 0:
        done = 8 - len([n for n in NUMS if not os.path.exists(os.path.join(DST, f"PRISM-2026-{n}-{NAMES[n]}.md"))])
        log.write(f"{t} intento {attempt}: {done}/8 rescatados\n")
    time.sleep(1)
log.close()
print("rescue_md terminado")
