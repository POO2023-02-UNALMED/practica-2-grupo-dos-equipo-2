''' Autores: Maria P. Ardila, Jose N. Duque, 
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard '''

from src.gestorAplicacion.sujeto.Restriccion import Restriccion
from src.gestorAplicacion.sujeto.Enfermedad import Enfermedad
from src.gestorAplicacion.serviciosOfrecidos.Ejercicio import Ejercicio

class Rutina:
    def __init__(self, paciente, tipoTerapia, tipoObjetivo):
        self._paciente = paciente
        self._tipoTerapia = tipoTerapia
        self._tipoObjetivo = tipoObjetivo
        self._restricciones = []
        self._ejerciciosPosibles = []
        self._cantidadEjercicios = 0
        self._ejerciciosOrdenados = []

        self.obtenerRestricciones()
        self.obtenerEjerciciosPosibles()

    def getCantidadEjercicios(self):
        return self._cantidadEjercicios

    def getEjerciciosPosibles(self):
        return self._ejerciciosPosibles

    def getRestricciones(self):
        return self._restricciones

    def setRestricciones(self, *args):
        self._restricciones.extend(list(args))
        self._ejerciciosPosibles = []
        self._obtenerEjerciciosPosibles()

    def getPaciente(self):
        return self._paciente

    def getEjerciciosOrdenados(self):
        return self._ejerciciosOrdenados

    def setEjerciciosOrdenados(self, ejerciciosOrdenados):
        self._ejerciciosOrdenados = ejerciciosOrdenados

    def agregarEjercicioOrdenado(self, ejercicio):
        self._ejerciciosOrdenados.append(ejercicio)

    def eliminarEjercicio(self, ejercicioEliminar):
        IDeliminar = ejercicioEliminar.getID()
        self._ejerciciosOrdenados = [ejercicio for ejercicio in self._ejerciciosOrdenados if ejercicio.getID() != IDeliminar]

    def obtenerRestricciones(self):
        listaEnfermedades = self._paciente.getHistoriaClinica().getHistorialEnfermedades()
        for enfermedad in listaEnfermedades:
            restriccionEnfermedad = enfermedad.getRestriccion()
            self._restricciones.append(restriccionEnfermedad)

    def obtenerEjerciciosPosibles(self):
        todosLosEjercicios = Ejercicio.get_ejercicios_totales()
        for ejercicio_a_revisar in todosLosEjercicios:
            restriccion_a_revisar = ejercicio_a_revisar.get_restriccion()
            terapia_a_revisar = ejercicio_a_revisar.get_tipoTerapia()
            objetivo_a_revisar = ejercicio_a_revisar.get_tipoObjetivo()
            if terapia_a_revisar == self._tipoTerapia:
                if objetivo_a_revisar == self._tipoObjetivo:
                    if not restriccion_a_revisar or restriccion_a_revisar not in self._restricciones:
                        self._ejerciciosPosibles.append(ejercicio_a_revisar)
        self._cantidadEjercicios = len(self._ejerciciosOrdenados)