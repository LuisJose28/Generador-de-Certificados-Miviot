import pandas as pd
import os
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from jinja2 import Template
import qrcode

def generar_codigo(i):
    return f"P10-AA{str(i + 1).zfill(4)}-2025"

# Crear carpetas de salida si no existen
os.makedirs("salida_certificados", exist_ok=True)
os.makedirs("salida_html", exist_ok=True)
os.makedirs("salida_qrs", exist_ok=True)

# Cargar datos desde el Excel
df = pd.read_excel("beneficiarios.xlsx")

# Cargar plantilla HTML
with open("plantilla.html", "r", encoding="utf-8") as f:
    plantilla_html = Template(f.read())

# Procesar cada fila del Excel
for i, row in df.iterrows():
    codigo = generar_codigo(i)

    # URL del QR (ruta oficial)
    qr_url = f"https://www.miviot.gob.pa/verificacion/aapartamentos/{codigo}.html"
    qr_path = os.path.join("salida_qrs", f"{codigo}.png")

    # Generar QR
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(qr_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_path)

    # ---------- Generar Certificado Word ----------
    tpl = DocxTemplate("plantilla.docx")
    context_word = {
        "apartamento": row["No. DE APARTAMENTO"],
        "torre": str(row["TORRE"]),
        "nombre": row["NOMBRE DEL BENEFICIARIO"],
        "cedula": str(row["CÉDULA"]),
        "resolucion": row["RESOLUCION"],
        "codigo": codigo,
        "qr": InlineImage(tpl, qr_path, width=Mm(30))
    }
    output_file_word = os.path.join("salida_certificados", f"certificado_{codigo}.docx")
    tpl.render(context_word)
    tpl.save(output_file_word)

    # ---------- Generar Certificado HTML ----------
    context_html = {
        "codigo": codigo,
        "proyecto": row["PROYECTO HABITACIONAL"],
        "nombre": row["NOMBRE DEL BENEFICIARIO"],
        "cedula": row["CÉDULA"],
        "torre": row["TORRE"],
        "apartamento": row["No. DE APARTAMENTO"],
        "valor": f"B/. {int(row['VALOR']):,}.00",
        "resolucion": row["RESOLUCION"],
        "provincia": row["PROVINCIA"]
    }
    html_render = plantilla_html.render(**context_html)
    output_file_html = os.path.join("salida_html", f"{codigo}.html")
    with open(output_file_html, "w", encoding="utf-8") as f:
        f.write(html_render)

print("✅ Certificados Word, HTML y QR generados correctamente.")
