"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from src.gestorAplicacion.sujeto.Medico import Medico
from src.gestorAplicacion.sujeto.Paciente import Paciente
from src.gestorAplicacion.serviciosOfrecidos.Tipo import Tipo
from src.gestorAplicacion.sujeto.Categoria import Categoria
from src.gestorAplicacion.sujeto.Categoria import Categoria
# Descripción: Esta clase representa una Cita en el sistema de administración hospitalaria.


class Cita:

    # Inicializador
    def __init__(self, medico, fecha, paciente, tipo, especialidad, categoria):
        self.medico = medico
        self.fecha = fecha
        self.paciente = paciente
        self.tipo = tipo
        self.especialidad = especialidad
        self.categoria = categoria

    # Getters y Setters
    def getMedico(self):
        return self.medico

    def setMedico(self, medico):
        self.medico = medico

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def getPaciente(self):
        return self.paciente

    def setPaciente(self, paciente):
        self.paciente = paciente
