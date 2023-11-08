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
    def guardarBanco(cls, banco):
        with open("src/baseDatos/temp/Banco.pkl", "wb") as archivo:
            pickle.dump(banco, archivo)
