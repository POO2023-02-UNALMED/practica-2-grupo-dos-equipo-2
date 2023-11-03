"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

import pickle
import os

# Clase encargada de la deserialización de objetos.


class Deserializador:

    # Carga un objeto desde el archivo especificado.
    """
    Parámetros:
    - ruta: Ruta donde se encuentra el objeto serializado.
    Retorna:
    - Objeto deserializado.
    """
    @staticmethod
    def cargarObjeto(ruta):
        with open(ruta, 'rb') as archivo:
            return pickle.load(archivo)

    # Carga una instancia del hospital.
    # Retorna: Instancia del hospital deserializada
    @staticmethod
    def cargarHospital():
        carpetaHospital = "baseDatos/temp/Hospital"
        rutaHospital = os.path.join(carpetaHospital, "hospital.pkl")
        return Deserializador.cargarObjeto(rutaHospital)

    # Carga una instancia del banco.
    # Retorna:Instancia del banco deserializada.
    @staticmethod
    def cargarBanco():
        carpetaBanco = "baseDatos/temp/Banco"
        rutaBanco = os.path.join(carpetaBanco, "banco.pkl")
        return Deserializador.cargarObjeto(rutaBanco)
