"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""
from src.gestorAplicacion.sujeto.Paciente import Paciente

class Habitacion:

    def __init__(self,numero):
        self._id = numero
        self._occupada = False
        self._paciente = None

    
    def reservarHabitacion(self,paciente):
        if(self._occupada == False):
            self._occupada = True
            self._paciente = paciente
            paciente.setHabitacion(self)

    def dejarHabitacion(self):
        if(self._occupada == True):
            self._occupada = False
            self._paciente.setHabitacion(None)
            self._paciente = None