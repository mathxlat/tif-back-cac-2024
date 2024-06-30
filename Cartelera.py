import mysql.connector
import mysql.connector.errorcode


class Cartelera:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        self.cursor = self.db.cursor()

        try:
            self.cursor.execute(f'USE {database}')
        except mysql.connector.Error as error:
            if error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f'CREATE DATABASE {database}')
                self.db.database = database
            else:
                raise error

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS peliculas (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                titulo VARCHAR(45) NOT NULL,
                                sinopsis VARCHAR(255) NOT NULL,
                                fecha_de_estreno date NOT NULL,
                                actores VARCHAR(45) NOT NULL,
                                genero VARCHAR(45) NOT NULL,
                                director VARCHAR(45) NOT NULL,
                                pais VARCHAR(45) NOT NULL,
                                duracion INT NOT NULL,
                                poster VARCHAR(255) NOT NULL,
                                trailer VARCHAR(255) NOT NULL)''')
        self.db.commit()

        self.cursor.close()
        self.cursor = self.db.cursor(dictionary=True)

    def obtener_peliculas(self):
        self.cursor.execute('SELECT * FROM peliculas')
        peliculas = self.cursor.fetchall()
        return peliculas

    def obtener_pelicula(self, id):
        self.cursor.execute('SELECT * FROM peliculas WHERE id = %s', id)
        return self.cursor.fetchone()

    def agregar_pelicula(self, titulo, sinopsis, fecha_de_estreno, actores, genero, director, pais, duracion, poster, trailer):
        sql = '''INSERT INTO peliculas (titulo,
                sinopsis,
                fecha_de_estreno,
                actores,
                genero,
                director,
                pais,
                duracion,
                poster,
                trailer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        values = (titulo, sinopsis, fecha_de_estreno, actores,
                  genero, director, pais, duracion, poster, trailer)
        self.cursor.execute(sql, values)
        self.db.commit()
        return self.cursor.lastrowid

    def modificar_pelicula(self, id, nuevo_titulo, nueva_sinopsis, nueva_fecha_de_estreno, nuevos_actores, nuevo_genero, nuevo_director, nuevo_pais, nueva_duracion, nuevo_poster, nuevo_trailer):
        sql = '''UPDATE peliculas SET 
                titulo = %s,
                sinopsis = %s,
                fecha_de_estreno = %s,
                actores = %s,
                genero = %s,
                director = %s,
                pais = %s,
                duracion = %s,
                poster = %s,
                trailer = %s WHERE id = %s'''
        valores = (nuevo_titulo, nueva_sinopsis, nueva_fecha_de_estreno, nuevos_actores,
                   nuevo_genero, nuevo_director, nuevo_pais, nueva_duracion, nuevo_poster, nuevo_trailer, id)
        self.cursor.execute(sql, valores)
        self.db.commit()
        return self.cursor.rowcount > 0

    def eliminar_pelicula(self, id):
        self.cursor.execute('DELETE FROM peliculas WHERE id = %s', id)
        self.db.commit()
        return self.cursor.rowcount > 0
