#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""backup.py — Respaldo resiliente del proyecto FUTURIA.
Copia los arboles criticos a FUTURIA-backup/ reintentando la lectura de cada
archivo hasta vencer el flake del mount MSYS. Genera MANIFEST-SHA256.md.
"""
import os, sys, hashlib, time, datetime

ROOT = os.getcwd()
BACKUP = "F:/"  # fallback; se sobreescribe abajo
BACKUP = os.path.join("C:/Users/getti", "FUTURIA-backup")
os.makedirs(BACKUP, exist_ok=True)

# (origen_relativo, [exclusiones de nombre])
TREES = [
    ("escenarios", []),
    ("metodologia", []),
    ("testing/escenarios", ["__pycache__"]),
    ("plataforma", ["__pycache__"]),
]
FILES = [
    "VERSIONADO.md",
    "migrate.py", "deploy_local.py", "gen_cards.py",
    "render_prism.py", "render_010.py", "manifest.txt",
]
SKILL = os.path.expanduser("~/AppData/Local/hermes/skills/prism-escenario")

def sha256(path, attempts=60, delay=0.5):
    for _ in range(attempts):
        try:
            h = hashlib.sha256()
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(65536), b""):
                    h.update(chunk)
            return h.hexdigest()
        except Exception:
            time.sleep(delay)
    return "ERROR_READ"

def copy_file(src, dst, man):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    data = None
    for _ in range(60):
        try:
            with open(src, "rb") as f:
                data = f.read()
            break
        except Exception:
            time.sleep(0.5)
    if data is None:
        print("  !! NO SE PUDO LEER", src)
        man.append((src, "FALLO_LECTURA", "0"))
        return
    with open(dst, "wb") as f:
        f.write(data)
    man.append((os.path.relpath(src, ROOT), sha256(src), str(len(data))))

def walk(tree, dst_root, excl, man):
    src_root = os.path.join(ROOT, tree)
    if not os.path.exists(src_root):
        print("  (omito", tree, "no existe)")
        return
    for dp, _, fns in os.walk(src_root):
        for fn in fns:
            if fn in excl or fn.endswith(".pyc"):
                continue
            src = os.path.join(dp, fn)
            rel = os.path.relpath(src, ROOT)
            dst = os.path.join(BACKUP, rel)
            copy_file(src, dst, man)

man = []
print("=== RESPALDO FUTURIA ===")
print("Origen:", ROOT)
print("Destino:", BACKUP)
for t, ex in TREES:
    print("-> arbol", t)
    walk(t, BACKUP, ex, man)
for f in FILES:
    if os.path.exists(os.path.join(ROOT, f)):
        print("-> archivo", f)
        copy_file(os.path.join(ROOT, f), os.path.join(BACKUP, f), man)
if os.path.exists(SKILL):
    print("-> skill prism-escenario")
    for dp, _, fns in os.walk(SKILL):
        for fn in fns:
            src = os.path.join(dp, fn)
            rel = os.path.relpath(src, os.path.expanduser("~/AppData/Local/hermes/skills"))
            dst = os.path.join(BACKUP, "skills", rel)
            copy_file(src, dst, man)

# Manifest
ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
lines = ["# MANIFEST DE INTEGRIDAD — RESPALDO FUTURIA", "", f"Generado: {ts}", f"Origen: {ROOT}", f"Total archivos: {len(man)}", "", "## Archivos", "", "| Relativo | Bytes | SHA-256 |", "|---|---|---|"]
for rel, sha, sz in sorted(man):
    lines.append(f"| {rel} | {sz} | {sha} |")
out = os.path.join(BACKUP, "MANIFEST-SHA256.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("\nManifest:", out, "archivos:", len(man))
fallos = [m for m in man if m[1] in ("FALLO_LECTURA", "ERROR_READ")]
if fallos:
    print("FALLOS:", fallos)
else:
    print("Sin fallos de lectura.")
print("DONE")
