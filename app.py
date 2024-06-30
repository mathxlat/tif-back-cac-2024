from flask import Flask, jsonify, request
from flask_cors import CORS
from Cartelera import Cartelera
from datetime import date

app = Flask(__name__)
CORS(app)

cartelera = Cartelera(host='localhost', user='root',
                      password='root', database='cartelera')


@app.route('/peliculas', methods=['GET'])
def obtener_peliculas():
    peliculas = cartelera.obtener_peliculas()
    return jsonify(peliculas)


@app.route('/peliculas', methods=['POST'])
def agregar_pelicula():
    titulo = request.form['titulo']
    sinopsis = request.form['sinopsis']
    fecha_de_estreno = date.fromisoformat(
        request.form['fecha_de_estreno'])
    actores = request.form['actores']
    genero = request.form['genero']
    director = request.form['director']
    pais = request.form['pais']
    duracion = request.form['duracion']
    poster = request.form['poster']
    trailer = request.form['trailer']

    id = cartelera.agregar_pelicula(
        titulo, sinopsis, fecha_de_estreno, actores, genero, director, pais, duracion, poster, trailer)

    if id:
        return jsonify({"mensaje": "Película agregada exitosamente", "id": id}), 201
    else:
        return jsonify({"mensaje": "Error al agregar la película"}), 500


@app.route('/peliculas/<int:id>', methods=['GET'])
def obtener_pelicula(id):
    pelicula = cartelera.obtener_pelicula(id)
    if pelicula:
        return jsonify(pelicula), 201
    else:
        return jsonify({"mensaje": "Película no encontrada"}), 404


@app.route('/peliculas/<int:id>', methods=['PUT'])
def modificar_pelicula(id):
    nuevo_titulo = request.form['titulo']
    nueva_sinopsis = request.form['sinopsis']
    nueva_fecha_de_estreno = date.fromisoformat(
        request.form['fecha_de_estreno'])
    nuevo_actores = request.form['actores']
    nuevo_genero = request.form['genero']
    nuevo_director = request.form['director']
    nuevo_pais = request.form['pais']
    nueva_duracion = request.form['duracion']
    nuevo_poster = request.form['poster']
    nuevo_trailer = request.form['trailer']

    pelicula = cartelera.obtener_pelicula(id)

    if pelicula:
        if cartelera.modificar_pelicula(id, nuevo_titulo, nueva_sinopsis, nueva_fecha_de_estreno, nuevo_actores,
                                        nuevo_genero, nuevo_director, nuevo_pais, nueva_duracion, nuevo_poster, nuevo_trailer):
            return jsonify({"mensaje": "Película modificada exitosamente"}), 200
        else:
            return jsonify({"mensaje": "Error al modificar la película"}), 500
    else:
        return jsonify({"mensaje": "Película no encontrada"}), 404


@app.route('/peliculas/<int:id>', methods=['DELETE'])
def eliminar_pelicula(id):
    pelicula = cartelera.obtener_pelicula(id)
    if pelicula:
        if cartelera.eliminar_pelicula(id):
            return jsonify({"mensaje": "Película eliminada exitosamente"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar la película"}), 500
    else:
        return jsonify({"mensaje": "Película no encontrada"}), 404


if __name__ == '__main__':
    app.run(debug=True)
