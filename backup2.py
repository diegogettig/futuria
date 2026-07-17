#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""backup2.py — Respaldo DIRIGIDO de archivos criticos, venciendo el flake del
mount: para cada patron, hace glob con reintentos hasta VER el archivo, y lo
copia en el acto (mismo proceso). Acumula en FUTURIA-backup/ sin sobrescribir.
"""
import os, shutil, time, glob

BACKUP = "C:/Users/getti/FUTURIA-backup"
os.makedirs(BACKUP, exist_ok=True)

PATTERNS = [
    "escenarios/PRISM-2026-000[1-9]-*.md",
    "escenarios/PRISM-2026-0010-*.md",
    "testing/escenarios/PRISM-2026-000[1-9]-*.yaml",
    "testing/escenarios/PRISM-2026-010-*.yaml",
    "testing/escenarios/assets/*",
    "metodologia/*",
    "plataforma/index.html",
    "plataforma/escenarios/*",
    "VERSIONADO.md", "migrate.py", "deploy_local.py", "gen_cards.py",
    "render_prism.py", "render_010.py", "manifest.txt", "backup.py",
]

def glob_until(pat, cycles=200, delay=0.3):
    for _ in range(cycles):
        try:
            r = glob.glob(pat)
            if r:
                return r
        except Exception:
            pass
        time.sleep(delay)
    return []

def copy_one(src):
    dst = os.path.join(BACKUP, os.path.relpath(src, os.getcwd()))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    return dst

total = 0
for pat in PATTERNS:
    found = glob_until(pat)
    for f in found:
        if os.path.isdir(f):
            for dp, _, fns in os.walk(f):
                for fn in fns:
                    d = os.path.join(dp, fn)
                    copy_one(d); total += 1
        else:
            copy_one(f); total += 1
    print(f"{pat}: {len(found)} encontrados")
print("Total copiados (adicionales):", total)
# re-manifest rapido
import hashlib
man = []
for dp, _, fns in os.walk(BACKUP):
    for fn in fns:
        p = os.path.join(dp, fn)
        try:
            h = hashlib.sha256(open(p,'rb').read()).hexdigest()
        except Exception:
            h = "ERR"
        man.append((os.path.relpath(p, BACKUP), len(open(p,'rb').read()) if h!='ERR' else 0, h))
ts = time.strftime("%Y-%m-%d %H:%M:%S")
L = ["# MANIFEST DE INTEGRIDAD — RESPALDO FUTURIA", "", f"Generado: {ts}", f"Total: {len(man)}", "", "| Relativo | Bytes | SHA-256 |", "|---|---|---|"]
for rel, sz, h in sorted(man):
    L.append(f"| {rel} | {sz} | {h} |")
open(os.path.join(BACKUP, "MANIFEST-SHA256.md"), "w", encoding="utf-8").write("\n".join(L)+"\n")
print("Manifest actualizado:", len(man), "archivos")
print("DONE")
