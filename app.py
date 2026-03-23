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
    
    
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            "id": len(books) + 1,
            "titulo": request.form['titulo'],
            "autor": request.form['autor'],
            "anio": request.form['anio'],
            "genero": request.form['genero']
        }
        books.append(new_book)
        return redirect(url_for('index'))
    return render_template('formulario.html', book=None)


@app.route('/delete/<int:id>')
def delete_book(id):
    global books
    books = [b for b in books if b['id'] != id]
    return redirect(url_for('index'))