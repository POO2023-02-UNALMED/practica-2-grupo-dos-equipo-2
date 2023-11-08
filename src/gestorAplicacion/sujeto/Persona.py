"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""


# Descripcion: Esta clase representa a una persona

class Persona():

    # Inicializador
    def __init__(self, categoria, numeroIdentificacion, nombre):
        self._categoria = categoria
        self._numeroIdentificacion = numeroIdentificacion
        self._nombre = nombre

    # Getters y Setters
    def getNombre(self):
        return self._nombre

    def getCategoria(self):
        return self._categoria

    def getNumeroIdentificacion(self):
        return self._numeroIdentificacion

    def setNombre(self, nombre):
        self._nombre = nombre

    def setCategoria(self, categoria):
        self._categoria = categoria

    def setNumeroIdentificacion(self, numeroIdentificacion):
        self._numeroIdentificacion = numeroIdentificacion
