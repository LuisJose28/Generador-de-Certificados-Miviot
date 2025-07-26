
# Proyecto de Automatización de Certificados de Adjudicación - MIVIOT

## 🎯 Objetivo del Proyecto

Desarrollar un sistema automatizado y escalable para la generación, verificación y validación de certificados de adjudicación de apartamentos para beneficiarios del Ministerio de Vivienda y Ordenamiento Territorial (MIVIOT). El proyecto incluye la creación de certificados físicos en formato Word, versiones digitales en formato HTML y códigos QR únicos para verificación en línea.

---

## 📊 Datos de Entrada

- **Archivo fuente:** `beneficiarios.xlsx`
- **Contenido:** Datos personales y técnicos de los beneficiarios, incluyendo:
  - Nombre del beneficiario
  - Cédula
  - Proyecto habitacional
  - Provincia, distrito, corregimiento
  - Torre, nivel, número de apartamento
  - Número de recámaras
  - Valor del apartamento

---

## 🧰 Herramientas y Tecnologías Utilizadas

- **Python**: Lógica de automatización
- **Pandas**: Lectura y manejo de datos desde Excel
- **docxtpl**: Generación de documentos Word desde plantilla
- **Jinja2**: Renderización de plantillas HTML
- **qrcode**: Generación de códigos QR personalizados
- **Netlify**: Hosting gratuito para certificados HTML
- **VS Code / Terminal**: Ejecución y pruebas locales

---

## 🗂 Estructura del Proyecto

```
/paquete_certificados/
├── beneficiarios.xlsx             # Datos de los beneficiarios
├── plantilla.docx                 # Plantilla para certificado Word
├── plantilla.html                 # Plantilla para certificado HTML
├── generar_certificados.py        # Genera certificados Word y QR
├── generar_html.py                # Genera certificados HTML
├── salida_certificados/           # Archivos Word generados
├── salida_html/                   # Archivos HTML generados
└── salida_qrs/                    # Códigos QR generados
```

---

## ⚙️ Funcionalidades

### ✅ Generación de Certificados Word

- A partir de una plantilla Word.
- Inserta automáticamente:
  - Datos del beneficiario
  - Código de adjudicación
  - Código QR con enlace verificable
- Guarda el archivo con nombre único como `certificado_Prueba-01.docx`.

### ✅ Generación de Certificados HTML

- Basado en plantilla `plantilla.html` inspirada en el diseño oficial de MIVIOT.
- Incluye todos los datos relevantes, más visualmente detallado.
- Compatible con navegación web móvil.
- Cada archivo se guarda como `Prueba-01.html`, `Prueba-02.html`, etc.

### ✅ Códigos QR

- Generados automáticamente para cada beneficiario.
- Enlazan al certificado HTML hospedado en Netlify u otro servidor.
- Son insertados en el documento Word y referenciados en HTML.

---

## 🔗 Lógica de Código

Los códigos únicos para cada beneficiario se generan con la lógica:

```
Prueba-01, Prueba-02, Prueba-03, ..., Prueba-500
```

Este código:
- Se muestra en el certificado
- Nombra el archivo Word y HTML
- Se utiliza como ruta final para el QR:
  `https://certificado-miviot.netlify.app/Prueba-01.html`

---

## 🌍 Publicación en Línea

- Los certificados HTML se suben a Netlify.
- Cada QR apunta al archivo HTML correspondiente.
- El beneficiario puede escanear el QR y validar su adjudicación en línea.

---

## 💡 Ventajas del Sistema

- 100% automatizado
- Consistente y profesional
- Adaptable a cambios de plantilla
- Escalable a cientos de beneficiarios
- Fácilmente validable con QR

---

## 🚀 Cómo Usar

1. Coloca `beneficiarios.xlsx`, `plantilla.docx` y `plantilla.html` en la raíz.
2. Ejecuta:

```bash
python generar_html.py          # Genera certificados HTML
python generar_certificados.py  # Genera certificados Word con QR
```

3. Sube la carpeta `salida_html` a Netlify u otro hosting.
4. Verifica escaneando cualquier QR desde un celular.

---

## 👨‍💻 Autor del Proyecto

**Luis Espinosa**  
Desarrollador y automatizador del proceso de adjudicación digital para MIVIOT.

---

Este proyecto optimiza tiempo, asegura exactitud en los datos y moderniza el proceso de entrega de certificados. Es una solución confiable, replicable y alineada con los estándares institucionales del MIVIOT.
