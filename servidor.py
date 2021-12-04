from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from datetime import date
import json

# para leer las fechas de la base de datos como string


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
CORS(app)
app.json_encoder = DateEncoder

# utilizando una base de datos en la nube
# servicio de ElephantSQL
conn = psycopg2.connect(
    host='ziggy.db.elephantsql.com',
    user='jlhnbbhm',
    database='jlhnbbhm',
    password='ZNt-0Xz6h2zq_GWs6YbzCjAlgtKbryQh'
)
cur = conn.cursor()

# 0 es domingo 6 es sabado


def convertir_dia(numero_dia: int):
    if numero_dia == 0:
        return 'Domingo'
    if numero_dia == 1:
        return 'Lunes'
    if numero_dia == 2:
        return 'Martes'
    if numero_dia == 3:
        return 'Miércoles'
    if numero_dia == 4:
        return 'Jueves'
    if numero_dia == 5:
        return 'Viernes'
    if numero_dia == 6:
        return 'Sábado'


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


@app.route('/funciones/<int:id_pelicula>')
def funciones(id_pelicula):
    cur.execute('''select extract(dow from fecha_hora), DATE(fecha_hora), butacas_disponibles, s.tipo 
	from funciones f inner join salas s on f.id_sala = s.id where id_pelicula = %s''',
                (id_pelicula,))
    datos = []
    for fila in cur.fetchall():
        datos.append({
            'dia': convertir_dia(int(fila[0])),
            'fecha': fila[1],
            'butacas': fila[2],
            'tipo': fila[3],
        })
    return jsonify(datos)


@app.route('/comprar', methods=['POST'])
def comprar():
    return


if __name__ == '__main__':
    app.run(debug=True)
