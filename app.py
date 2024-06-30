from flask import Flask, jsonify, request
from flask_cors import CORS
from Cartelera import Cartelera

app = Flask(__name__)
CORS(app)

cartelera = Cartelera(host='localhost', user='root', password='root', database='cartelera')

@app.route('/peliculas', methods=['GET'])
def obtener_peliculas():
    peliculas = cartelera.obtener_peliculas()
    return jsonify(peliculas)


@app.route('/peliculas', methods=['POST'])
def agregar_pelicula():
    pass


@app.route('/peliculas/<int:id>', methods=['GET'])
def obtener_pelicula(id):
    pelicula = cartelera.obtener_pelicula(id)
    if pelicula:
        return jsonify(pelicula), 201
    else:
        return "Pelicula no encontrada", 404


@app.route('/peliculas/<int:id>', methods=['PUT'])
def modificar_pelicula():
    pass


@app.route('/peliculas/<int:id>', methods=['DELETE'])
def eliminar_pelicula():
    pass


if __name__ == '__main__':
    app.run(debug=True)
