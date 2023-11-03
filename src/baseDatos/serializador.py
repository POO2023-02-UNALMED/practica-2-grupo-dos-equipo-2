"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

import pickle
import os

# Clase encargada de la serialización de objetos.


class Serializador:

    # Guarda un objeto en el archivo especificado.
    """
    Parámetros:
    - objeto: Objeto que se desea serializar.
    - ruta: Ruta donde se desea guardar el objeto serializado.
    """
    @staticmethod
    def guardarObjeto(objeto, ruta):
        # with-as abre y cierra el archivo automaticamente
        with open(ruta, 'wb') as archivo:
            pickle.dump(objeto, archivo)

    # Guarda una instancia del hospital.
    # Parámetros: hospital: Instancia del hospital que se desea guardar.
    @staticmethod
    def guardarHospital(hospital):
        carpetaHospital = "baseDatos/temp/Hospital"
        os.makedirs(carpetaHospital, exist_ok=True)

        # Guarda la instancia del hospital
        rutaHospital = os.path.join(carpetaHospital, "hospital.pkl")
        Serializador.guardarObjeto(hospital, rutaHospital)

    # Guarda una instancia del banco.
    # Parámetros: banco: Instancia del banco que se desea guardar.
    @staticmethod
    def guardarBanco(banco):
        carpetaBanco = "baseDatos/temp/Banco"
        os.makedirs(carpetaBanco, exist_ok=True)

        # Guarda la instancia del banco
        rutaBanco = os.path.join(carpetaBanco, "banco.pkl")
        Serializador.guardarObjeto(banco, rutaBanco)
