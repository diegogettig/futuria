#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""git_save.py — Salva los .md fuente de escenarios en git con reintentos
agresivos para vencer el flake del mount MSYS. Hace git add de cada archivo
hasta que git lo vea staged, luego commit. Correr en background.
"""
import subprocess, os, time, datetime

ROOT = os.getcwd()
FILES = [
    "escenarios/PRISM-2026-0002-sociedades-automatizadas.md",
    "escenarios/PRISM-2026-0003-cardio-bionico.md",
    "escenarios/PRISM-2026-0004-hard-tech-foundations.md",
    "escenarios/PRISM-2026-0005-gobernanza-algoritmica.md",
    "escenarios/PRISM-2026-0006-longevidad-caas.md",
    "escenarios/PRISM-2026-0007-conciencia-verificable.md",
    "escenarios/PRISM-2026-0008-bioprinting-distribuido.md",
    "escenarios/PRISM-2026-0009-geopolitica-datos.md",
    "fix_yaml.py", "render_prism.py", "render_010.py",
]

def git(*a):
    return subprocess.run(["git"]+list(a), cwd=ROOT, capture_output=True, text=True)

def staged(name):
    r = git("diff","--cached","--name-only")
    return name in r.stdout.split()

log = open(os.path.join(ROOT,"git_save.log"),"a",encoding="utf-8")
for attempt in range(1, 400):  # hasta ~ muchos intentos
    t = datetime.datetime.now().strftime("%H:%M:%S")
    changed = False
    for f in FILES:
        if staged(f):
            continue
        # intentar add (falla silenciosamente si el mount oculta el archivo)
        r = git("add", f)
        if staged(f):
            log.write(f"{t} STAGED {f}\n"); changed = True
    staged_now = [f for f in FILES if staged(f)]
    if len(staged_now) == len(FILES):
        msg = f"FUTURIA: respaldo git de fuentes escenarios 0002-0009 + scripts (intento {attempt})"
        git("commit", "-q", f"-m{msg}")
        log.write(f"{t} COMMIT hecho. archivos staged={len(staged_now)}\n")
        break
    if attempt % 20 == 0:
        log.write(f"{t} intento {attempt}: staged {len(staged_now)}/{len(FILES)}\n")
    time.sleep(1.5)
log.close()
print("git_save terminado")
