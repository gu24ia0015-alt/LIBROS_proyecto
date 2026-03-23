from flask import Flask, render_template

app = Flask(__name__)

books = [
    {"id": 1, "titulo": "El Quijote", "autor": "Miguel de Cervantes", "anio": "1605", "genero": "Novela"}
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)