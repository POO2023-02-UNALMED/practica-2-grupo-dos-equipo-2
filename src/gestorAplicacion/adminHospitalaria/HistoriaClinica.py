"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from src.gestorAplicacion.sujeto.Paciente import Paciente
from src.gestorAplicacion.sujeto.Enfermedad import Enfermedad
from src.gestorAplicacion.adminHospitalaria.OrdenMedica import OrdenMedica
from src.gestorAplicacion.serviciosOfrecidos.Terapia import Terapia
from src.gestorAplicacion.serviciosOfrecidos.Cirugia import Cirugia
from src.gestorAplicacion.serviciosOfrecidos.Consulta import Consulta
# Descripción: Esta clase representa una Historia Clínica en el sistema de administración hospitalaria.


class HistoriaClinica:

    # Inicializador
    def __init__(self, paciente):
        self._PACIENTE = paciente
        self._historialEnfermedades = []
        self._historialOrdenes = []
        self._historialTerapias = []
        self._historialCirugias = []
        self._historialConsultas = []
        self._historialRutinas = []
        self._historialCitas = []

    # Getters y Setters
    def getPACIENTE(self):
        return self._PACIENTE

    def getHistorialEnfermedades(self):
        return self._historialEnfermedades

    def setHistorialEnfermedades(self, historialEnfermedades):
        self._historialEnfermedades = historialEnfermedades

    def getHistorialOrdenes(self):
        return self._historialOrdenes

    def setHistorialOrdenes(self, historialOrdenes):
        self._historialOrdenes = historialOrdenes

    def getHistorialTerapias(self):
        return self._historialTerapias

    def setHistorialTerapias(self, historialTerapias):
        self._historialTerapias = historialTerapias

    def getHistorialCirugias(self):
        return self._historialCirugias

    def setHistorialCirugias(self, historialCirugias):
        self._historialCirugias = historialCirugias

    def getHistorialConsultas(self):
        return self._historialConsultas

    def setHistorialConsultas(self, historialConsultas):
        self._historialConsultas = historialConsultas

    def getHistorialRutinas(self):
        return self._historialRutinas

    def setHistorialRutinas(self, historialRutinas):
        self._historialRutinas = historialRutinas

    def getHistorialCitas(self):
        return self._historialCitas

    def setHistorialCitas(self, historialCitas):
        self._historialCitas = historialCitas
