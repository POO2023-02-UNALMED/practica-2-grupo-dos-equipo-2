"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

import pickle

# Clase encargada de la serialización de objetos.


class Serializador:

    @classmethod
    def guardarHospital(cls, hospital):
        with open("src/baseDatos/temp/Hospital.pkl", "wb") as archivo:
            pickle.dump(hospital, archivo)

    @classmethod
    def serializarAtributosEstaticos(cls, hospital):
        with open("src/baseDatos/temp/Pacientes.pkl", "wb") as archivo:
            pickle.dump(hospital.getPacientes(), archivo)
        with open("src/baseDatos/temp/Medicos.pkl", "wb") as archivo:
            pickle.dump(hospital.getMedicos(), archivo)
        with open("src/baseDatos/temp/Enfermedades.pkl", "wb") as archivo:
            pickle.dump(hospital.getEnfermedades(), archivo)

    @classmethod
    def guardarBanco(cls, banco):
        with open("src/baseDatos/temp/Banco.pkl", "wb") as archivo:
            pickle.dump(banco, archivo)
