import pandas as pd
import os
from jinja2 import Template

df = pd.read_excel("beneficiarios.xlsx")
os.makedirs("salida_html", exist_ok=True)

with open("plantilla.html", "r", encoding="utf-8") as f:
    plantilla_html = Template(f.read())

for i, row in df.iterrows():
    codigo = f"P03-AA{str(i + 1).zfill(4)}-2025"

    html_render = plantilla_html.render(
        codigo=codigo,
        proyecto=row["PROYECTO HABITACIONAL"],
        nombre=row["NOMBRE DEL BENEFICIARIO"],
        cedula=row["CÉDULA"],
        torre=row["TORRE"],
        apartamento=row["No. DE APARTAMENTO"],
        valor=f"B/. {int(row['VALOR']):,}.00",        
        resolucion=row["RESOLUCION"],
        provincia=row["PROVINCIA"]
    )

    with open(os.path.join("salida_html", f"{codigo}.html"), "w", encoding="utf-8") as f:
        f.write(html_render)

print("✅ Certificados HTML actualizados correctamente.")
