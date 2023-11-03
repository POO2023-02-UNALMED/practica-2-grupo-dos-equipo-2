"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from instalaciones import Hospital
from Persona import Persona


class Medico(Persona):

    # Inicializador
    def __init__(self, categoria, numeroIdentificacion, nombre, especialidad):
        super().__init__(categoria, numeroIdentificacion, nombre)
        self._especialidad = especialidad
        self._agenda = []
        Hospital.anadirMedicos(self)

    # Getters y Setters
    def getEspecialidad(self):
        return self._especialidad

    def setEspecialidad(self, especialidad):
        self._especialidad = especialidad

    def getAgenda(self):
        return self._agenda

    def setAgenda(self, agenda):
        self._agenda = agenda
