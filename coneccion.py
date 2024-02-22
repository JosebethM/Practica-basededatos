from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mostrar_datos():
    conn = sqlite.connect('estudiantes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    datos = cursor.fetchall()
    conn.close()

    return render_template('index.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)