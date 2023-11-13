"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from gestorAplicacion.sujeto import TipoTerapia, TipoObjetivo, Restriccion

# Descripción: Esta clase se encarga ...

class CaracteristicasEjercicio:
    def __init__(self, tipoTerapia, objetivo, restriccion):
        self.tipoTerapia = tipoTerapia
        self.objetivo = objetivo
        self.restriccion = restriccion

    # Getters y setters para TipoTerapia
    def getTipoTerapia(self):
        return self.tipoTerapia

    def setTipoTerapia(self, tipoTerapia):
        self.tipoTerapia = tipoTerapia

    # Getters y setters para TipoObjetivo
    def getTipoObjetivo(self):
        return self.objetivo

    def setTipoObjetivo(self, objetivo):
        self.objetivo = objetivo

    # Getters y setters para Restriccion
    def getRestriccion(self):
        return self.restriccion

    def setRestriccion(self, restriccion):
        self.restriccion = restriccion