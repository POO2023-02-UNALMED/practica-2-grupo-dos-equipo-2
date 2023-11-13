''' Autores: Maria P. Ardila, Jose N. Duque, 
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard '''

from gestorAplicacion.sujeto import Ejercicio, Restriccion, Enfermedad, CaracteristicasEjercicio

class Rutina:
    def __init__(self, paciente, tipoTerapia, tipoObjetivo):
        self.paciente = paciente
        self.tipoTerapia = tipoTerapia
        self.tipoObjetivo = tipoObjetivo
        self.restricciones = []
        self.ejerciciosPosibles = []
        self.cantidadEjercicios = 0
        self.ejerciciosOrdenados = []

        self.obtenerRestricciones()
        self.obtenerEjerciciosPosibles()

    def getCantidadEjercicios(self):
        return self.cantidadEjercicios

    def getEjerciciosPosibles(self):
        return self.ejerciciosPosibles

    def getRestricciones(self):
        return self.restricciones

    def setRestricciones(self, args):
        nuevasRestricciones = list(args)
        self.restricciones.extend(nuevasRestricciones)
        self.ejerciciosPosibles = []
        self.obtenerEjerciciosPosibles()

    def getPaciente(self):
        return self.paciente

    def getEjerciciosOrdenados(self):
        return self.ejerciciosOrdenados

    def setEjerciciosOrdenados(self, ejerciciosOrdenados):
        self.ejerciciosOrdenados = ejerciciosOrdenados

    def agregarEjercicioOrdenado(self, ejercicio):
        self.ejerciciosOrdenados.append(ejercicio)

    def eliminarEjercicio(self, ejercicioEliminar):
        IDeliminar = ejercicioEliminar.getID()
        self.ejerciciosOrdenados = [ejercicio for ejercicio in self.ejerciciosOrdenados if ejercicio.getID() != IDeliminar]

    def obtenerRestricciones(self):
        listaEnfermedades = self.paciente.getHistoriaClinica().getHistorialEnfermedades()
        for enfermedad in listaEnfermedades:
            restriccionEnfermedad = enfermedad.getRestriccion()
            self.restricciones.append(restriccionEnfermedad)

    def obtenerEjerciciosPosibles(self):
        todosLosEjercicios = list(Ejercicio)
        for ejercicioEnum in todosLosEjercicios:
            caracteristicasEjercicio = ejercicioEnum.getEjercicio()
            restriccionARevisar = caracteristicasEjercicio.getRestriccion()
            if caracteristicasEjercicio.getTipoTerapia() == self.tipoTerapia:
                if caracteristicasEjercicio.getTipoObjetivo() == self.tipoObjetivo:
                    if restriccionARevisar not in self.restricciones:
                        self.ejerciciosPosibles.append(ejercicioEnum)
        self.cantidadEjercicios = len(self.ejerciciosOrdenados)