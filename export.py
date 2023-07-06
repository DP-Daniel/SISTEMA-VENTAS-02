from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas



# Crear un archivo PDF con ReportLab
c = Canvas("inventario.pdf", pagesize=letter)
width, height = letter

# Dibujar el título en una posición específica
c.drawString(200 / 2, height - inch, "Reporte de inventario")

# Dibujar la imagen en una posición específica
c.drawImage("logo.jpg", width - 2 * inch, height - inch, width=inch, height=inch)