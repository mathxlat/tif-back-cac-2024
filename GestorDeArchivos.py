from werkzeug.utils import secure_filename
import os
import uuid


class GestorDeArchivos:
    def __init__(self, ruta_destino, extensiones_permitidas):
        self.ruta_destino = ruta_destino
        self.extensiones_permitidas = extensiones_permitidas

    def es_archivo_permitido(self, nombre_archivo: str):
        extension = nombre_archivo.rsplit('.', 1)[1].lower()

        return '.' in nombre_archivo and extension in self.extensiones_permitidas

    def generar_ruta_archivo(self, archivo):
        if archivo and self.es_archivo_permitido(archivo.filename):
            nombre_archivo_seguro = secure_filename(archivo.filename).lower()
            identificador_unico = uuid.uuid4().hex
            nombre_archivo_unico = f"{identificador_unico}-{nombre_archivo_seguro}"
            ruta_archivo = os.path.join(
                self.ruta_destino, nombre_archivo_unico)
            return ruta_archivo

        return None

    def guardar_archivo(self, archivo, ruta_archivo):
        archivo.save(ruta_archivo)

    def modificar_archivo(self, archivo_nuevo, ruta_archivo_nuevo, ruta_archivo_existente):
        self.eliminar_archivo(ruta_archivo_existente)

        self.guardar_archivo(archivo_nuevo, ruta_archivo_nuevo)

    def eliminar_archivo(self, ruta_archivo):
        existe_ruta_archivo = os.path.exists(ruta_archivo)

        if existe_ruta_archivo:
            os.remove(ruta_archivo)

        return existe_ruta_archivo
