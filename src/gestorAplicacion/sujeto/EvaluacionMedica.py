"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

#Clase que hará la evaluación médica
class EvaluacionMedica:

    def __init__(self,nombre,especialidad):
        self._nombre=nombre
        self._especialidad=especialidad

    #getters y setters
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre=nombre

    def getEspecialidad(self):
        return self._especialidad

    def setEspecialidad(self, especialidad):
        self._especialidad=especialidad        