from flask import Flask, render_template, request, jsonify
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario
@app.route('/submit', methods=['POST'])
def submit():
    # Recoge los datos del formulario
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    dni = request.form['dni']
    address = request.form['address']

    # Genera el PDF
    pdf_file = generate_pdf(name, last_name, email, dni, address)

    # Retorna el nombre del archivo PDF generado
    return jsonify({'pdf_file': pdf_file})

# Función para generar el PDF
def generate_pdf(name, last_name, email, dni, address):
    pdf_file = f"{name}_{last_name}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Agrega el texto al PDF
    c.drawString(100, 750, "Nombre: " + name)
    c.drawString(100, 730, "Apellido: " + last_name)
    c.drawString(100, 710, "Email: " + email)
    c.drawString(100, 690, "DNI: " + dni)
    c.drawString(100, 670, "Dirección: " + address)

    # Guarda el PDF
    c.save()

    return pdf_file

if __name__ == '__main__':
    app.run(debug=True)
