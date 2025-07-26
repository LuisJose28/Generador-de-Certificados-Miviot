# Objetivo: Generar archivos Word (.docx) personalizados para cada beneficiario, insertando sus datos y un código QR que apunta al certificado HTML en línea.

#Importar las librerías necesarias:
import pandas as pd
import os
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import qrcode

#Función para generar códigos únicos
def generar_codigo(i):
    return f"P03-AA{str(i + 1).zfill(4)}-2025"

#Crea carpetas para guardar los archivos Word generados y los QR, si no existen.
os.makedirs("salida_certificados", exist_ok=True)
os.makedirs("salida_qrs", exist_ok=True)

df = pd.read_excel("beneficiarios.xlsx")

#Itera fila por fila en el Excel para generar un certificado por beneficiario
for i, row in df.iterrows():
    tpl = DocxTemplate("plantilla.docx") #Carga la plantilla Word donde se insertarán los datos dinámicamente.

    codigo = generar_codigo(i)
    apartamento = row["No. DE APARTAMENTO"]
    torre = str(row["TORRE"])
    nombre = row["NOMBRE DEL BENEFICIARIO"]
    cedula = str(row["CÉDULA"])
    resolucion = row["RESOLUCION"]

    # Genera el código único del certificado y crea el enlace del QR apuntando a su HTML en Netlify.
    url = f"https://www.miviot.gob.pa/verificacion/aapartamentos/{codigo}.html"


    # Genera la imagen del código QR y la guarda en salida_qrs/.
    qr_path = os.path.join("salida_qrs", f"{codigo}.png")
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_path)

    context = {
        "apartamento": apartamento,
        "torre": torre,
        "nombre": nombre,
        "cedula": cedula,
        "resolucion": resolucion,
        "codigo": codigo,
        "qr": InlineImage(tpl, qr_path, width=Mm(30))
    }

    output_file = os.path.join("salida_certificados", f"certificado_{codigo}.docx")
    #Inserta los datos en el Word y lo guarda como certificado_Prueba-01.docx, etc.
    tpl.render(context)
    tpl.save(output_file)

print("✅ Certificados generados.")
