from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# utilizando una base de datos en la nube
# servicio de ElephantSQL
conn = psycopg2.connect(
    host='ziggy.db.elephantsql.com',
    user='jlhnbbhm',
    database='jlhnbbhm',
    password='ZNt-0Xz6h2zq_GWs6YbzCjAlgtKbryQh'
)
cur = conn.cursor()


@app.route('/')
def index():
    return '<h3>Hello World desde Flask! - Sistema Cine Serna</h3>'


@app.route('/peliculas')
def peliculas():
    cur.execute('select * from peliculas')
    datos = []
    for fila in cur.fetchall():
        datos.append({
            'id': fila[0],
            'titulo': fila[1],
            'sinopsis': fila[2],
            'duracion': fila[3],
            'link_trailer': fila[4],
            'link_portada': fila[5],
            'tipo': fila[6],
        })
    return jsonify(datos)


@app.route('/pelicula/<int:id_pelicula>')
def pelicula(id_pelicula):
    cur.execute('select * from peliculas where id = %s', (id_pelicula,))
    datos = cur.fetchone()
    return {
        'titulo': datos[1],
        'sinopsis': datos[2],
        'duracion': datos[3],
        'link_trailer': datos[4],
        'link_portada': datos[5],
        'tipo': datos[6],
    }


@app.route('/funciones', methods=['POST'])
def funciones():
    return


@app.route('/comprar', methods=['POST'])
def comprar():
    return


if __name__ == '__main__':
    app.run(debug=True)
