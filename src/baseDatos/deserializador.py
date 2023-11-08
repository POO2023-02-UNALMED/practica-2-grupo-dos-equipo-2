"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

import pickle

# Clase encargada de la deserialización de objetos.


class Deserializador:
    # Carga una instancia del hospital.
    # Retorna: Instancia del hospital deserializada
    @classmethod
    def cargarHospital(cls):
        with open("src/baseDatos/temp/Hospital.pkl", "rb") as archivo:
            return pickle.load(archivo)

    @classmethod
    def deserializarAtributosEstaticos(cls, hospital):
        hospital.limpiarDatos()
        with open("src/baseDatos/temp/Pacientes.pkl", "rb") as archivo:
            hospital.setPacientes(pickle.load(archivo))
        with open("src/baseDatos/temp/Medicos.pkl", "rb") as archivo:
            hospital.setMedicos(pickle.load(archivo))
        with open("src/baseDatos/temp/Enfermedades.pkl", "rb") as archivo:
            hospital.setEnfermedades(pickle.load(archivo))

    # Carga una instancia del banco.
    # Retorna:Instancia del banco deserializada.
    @classmethod
    def cargarBanco(cls):
        with open("src/baseDatos/temp/Banco.pkl", "rb") as archivo:
            return pickle.load(archivo)
