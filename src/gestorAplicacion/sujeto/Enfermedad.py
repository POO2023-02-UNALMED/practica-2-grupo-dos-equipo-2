"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""


from instalaciones import Hospital
from sujeto import EvaluacionMedica

# Clase que representa una enfermedad en el sistema médico


class Enfermedad(EvaluacionMedica):

    # Inicializador
    def __init__(self, nombre, especialidad, tipologia, sintomas, restricciones):
        super().__init__(nombre, especialidad)
        self.tipologia = tipologia
        self.sintomas = sintomas
        self.restricciones = restricciones
        Hospital.anadirEnfermedades(self)

    # Getters y Setters
    def getTipologia(self):
        return self.tipologia

    def setTipologia(self, tipologia):
        self.tipologia = tipologia

    def getSintomas(self):
        return self.sintomas

    def setSintomas(self, sintomas):
        self.sintomas = sintomas

    def getRestricciones(self):
        return self.restricciones

    def setRestricciones(self, restricciones):
        self.restricciones = restricciones
