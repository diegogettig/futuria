#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FUTURIA · Generador de PDF protegido con marca de agua.

Convierte un .md (o .html) en un PDF con:
  - Marca de agua diagonal "FUTURIA · CONFIDENCIAL" en cada pagina (via PIL -> PNG).
  - Proteccion por cifrado (owner password + restriccion de copia/modificacion;
    impresion permitida). User password opcional.
  - Encabezado/pie con trazabilidad (origen, fecha, numero de control).

Uso:
  python build_pdf.py entrada.md --out salida.pdf \
      --watermark "FUTURIA · CONFIDENCIAL" \
      --owner "FUTURIA-OWNER-2026" --user "" \
      --titulo "Proyeccion Sectorial: Grupo SanCor Salud"
"""
import argparse, sys, os, datetime
import markdown
from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont

ANCHO_PT, ALTO_PT = 595.28, 841.89  # A4

def generar_marca_de_agua(texto, path, angulo=-30):
    """Crea un PNG transparente con el texto repetido en diagonal."""
    ancho, alto = int(ANCHO_PT), int(ALTO_PT)
    img = Image.new("RGBA", (ancho, alto), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 42)
    except Exception:
        font = ImageFont.load_default()
    # repetir el texto en mosaico cubriendo el lienzo
    step_x, step_y = 260, 150
    for y in range(-alto, alto, step_y):
        for x in range(-ancho, ancho, step_x):
            d.text((x, y), texto, font=font, fill=(120, 120, 130, 55))
    # rotar toda la imagen
    img = img.rotate(angulo, expand=False, center=(ancho // 2, alto // 2))
    img.save(path, "PNG")
    return path

class PDFConMarca(FPDF):
    def __init__(self, watermark_png, control, titulo):
        super().__init__(orientation="P", unit="pt", format="A4")
        self.set_auto_page_break(True, margin=60)
        self.wm = watermark_png
        self.control = control
        self.titulo = titulo
        self.set_margins(54, 54, 54)

    def header(self):
        if self.page_no() == 1:
            return  # la portada tiene su propio diseno
        # marca de agua centrada
        try:
            self.image(self.wm, x=0, y=0, w=self.w, h=self.h)
        except Exception:
            pass
        self.set_font("Helvetica", "I", 7.5)
        self.set_text_color(150, 150, 160)
        self.set_y(20)
        self.cell(0, 8, "FUTURIA · INSTITUTO GLOBAL DE FUTUROS PLAUSIBLES", align="L")
        self.cell(0, 8, self.control, align="R")
        self.set_text_color(0, 0, 0)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-42)
        try:
            self.image(self.wm, x=0, y=0, w=self.w, h=self.h)
        except Exception:
            pass
        self.set_font("Helvetica", "I", 7.5)
        self.set_text_color(150, 150, 160)
        self.cell(0, 8, "Documento confidencial · No copiar ni redistribuir sin autorizacion", align="L")
        self.cell(0, 8, "Pagina %d" % self.page_no(), align="R")
        self.set_text_color(0, 0, 0)

def html_a_pdf(md_path, out_path, watermark="FUTURIA · CONFIDENCIAL",
               owner="FUTURIA-OWNER-2026", user="", titulo="Informe FUTURIA",
               control="", nivel="abre-libre"):
    base = os.path.dirname(os.path.abspath(out_path))
    wm_png = os.path.join(base, "_wm_tmp.png")
    generar_marca_de_agua(watermark, wm_png)
    from fpdf.enums import EncryptionMethod, AccessPermission
    if nivel == "con_password":
        user_pass = user or "FUTURIA-2026"
        perms = AccessPermission.PRINT_LOW_RES | AccessPermission.PRINT_HIGH_RES
    elif nivel == "quemado":
        user_pass = user
        perms = AccessPermission.PRINT_LOW_RES | AccessPermission.PRINT_HIGH_RES
    else:  # abre-libre
        user_pass = user
        perms = AccessPermission.PRINT_LOW_RES | AccessPermission.PRINT_HIGH_RES
    html = markdown.markdown(open(md_path, encoding="utf-8").read(),
                             extensions=["tables", "fenced_code"])
    pdf = PDFConMarca(wm_png, control, titulo)
    pdf.set_title(titulo)
    pdf.set_author("FUTURIA Institute")
    # portada
    pdf.add_page()
    pdf.set_fill_color(10, 10, 16); pdf.rect(0, 0, pdf.w, pdf.h, "F")
    try:
        pdf.image(wm_png, x=0, y=0, w=pdf.w, h=pdf.h)
    except Exception:
        pass
    ancho = pdf.w - 108
    pdf.set_xy(54, pdf.h / 2 - 130)
    pdf.set_text_color(245, 80, 48)
    pdf.set_font("Helvetica", "B", 30)
    pdf.set_x(54); pdf.multi_cell(ancho, 34, titulo, align="C")
    pdf.set_text_color(230, 230, 235)
    pdf.set_font("Helvetica", "", 13)
    pdf.set_x(54); pdf.multi_cell(ancho, 20, "Observatorio de Vigilancia Estrategica . FUTURIA Institute", align="C")
    pdf.set_x(54); pdf.multi_cell(ancho, 18, "Prospeccion de Negocios . Prospectiva con trazabilidad", align="C")
    pdf.set_text_color(150, 150, 160)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_x(54); pdf.multi_cell(ancho, 14, "Fecha: %s   |   Control: %s" % (datetime.date.today().isoformat(), control), align="C")
    pdf.set_text_color(0, 0, 0)
    # cuerpo
    pdf.add_page()
    pdf.write_html(html)
    # proteccion
    pdf.set_encryption(owner_password=owner, user_password=user_pass,
                       encryption_method=EncryptionMethod.RC4, permissions=perms)
    pdf.output(out_path)
    try:
        os.remove(wm_png)
    except Exception:
        pass
    return out_path

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada")
    ap.add_argument("--out", default="salida.pdf")
    ap.add_argument("--watermark", default="FUTURIA · CONFIDENCIAL")
    ap.add_argument("--owner", default="FUTURIA-OWNER-2026")
    ap.add_argument("--user", default="")
    ap.add_argument("--titulo", default="Informe FUTURIA")
    ap.add_argument("--control", default="")
    ap.add_argument("--nivel", default="abre-libre",
                    choices=["abre-libre", "con_password", "quemado"])
    a = ap.parse_args()
    ruta = html_a_pdf(a.entrada, a.out, a.watermark, a.owner, a.user, a.titulo, a.control, a.nivel)
    print("PDF generado:", ruta)
