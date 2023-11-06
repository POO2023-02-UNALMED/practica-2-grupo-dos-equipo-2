"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from abc import ABC, abstractmethod
from src.gestorAplicacion.adminHospitalaria.Cita import Cita
from src.gestorAplicacion.sujeto.EvaluacionMedica import EvaluacionMedica

# Descripción: Esta clase abstracta representa un tratamiento médico


class Tratamiento (ABC, EvaluacionMedica):

    # Inicializador
    def __init__(self, nombre, especialidad, enfermedad, cita):
        super().__init__(nombre, especialidad)
        self._enfermedad = enfermedad
        self._pagada = False
        self._cita = cita

    # Método abstracto para calcular el precio del tratamiento para un paciente.
    @abstractmethod
    def calcularPrecio(paciente):
        pass

    # Método abstracto para representar el tratamiento como cadena de texto.
    @abstractmethod
    def __str__(self):
        pass

    # Marcar el tratamiento como pagado.
    def marcarComoPagada(self):
        self.pagada = True

    # Getters y Setters

    def getEnfermedad(self):
        return self._enfermedad

    def getEspecialidad(self):
        return self._especialidad

    def isPagada(self):
        return self._pagada

    def getCita(self):
        return self._cita

    def setEnfermedad(self, enfermedad):
        self._enfermedad = enfermedad

    def setEspecialidad(self, especialidad):
        self._especialidad = especialidad

    def setPagada(self, pagada):
        self._pagada = pagada

    def setCita(self, cita):
        self._cita = cita
