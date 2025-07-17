# Objetivo: Generar certificados en HTML para cada beneficiario con todos sus datos y QR enlazado.

#Importar las librerías necesarias:
import pandas as pd
import os
from jinja2 import Template

# Cargar los datos del Excel
df = pd.read_excel("beneficiarios.xlsx")

# Crear carpeta de salida si no existe
os.makedirs("salida_html", exist_ok=True)

# Carga la plantilla HTML base y la prepara para insertar los valores dinámicos
with open("plantilla.html", "r", encoding="utf-8") as f:
    plantilla_html = Template(f.read())

# Generar HTML por cada fila del Excel
for i, row in df.iterrows():
    codigo = f"Prueba-{i+1:02d}"  # Genera el mismo código único que en el script anterior.

    # Inserta los datos en la plantilla HTML
    html_render = plantilla_html.render(
        codigo=codigo,
        nombre=row["NOMBRE DEL BENEFICIARIO"],
        cedula=row["CÉDULA"],
        proyecto=row["PROYECTO HABITACIONAL"],
        provincia=row["PROVINCIA"],
        distrito=row["DISTRITO"],
        corregimiento=row["CORREGIMIENTO"],
        torre=row["TORRE"],
        nivel=row["NIVEL"],
        apartamento=row["No. DE APARTAMENTO"],
        recamaras=row["RECÁMARAS"],
        valor=row["VALOR"]



    )

    # Guardar archivo HTML
    salida_path = os.path.join("salida_html", f"{codigo}.html")
    #Guarda el archivo HTML en la carpeta salida_html.
    with open(salida_path, "w", encoding="utf-8") as f:
        f.write(html_render)

print("✅Archivos HTML generados correctamente.")
