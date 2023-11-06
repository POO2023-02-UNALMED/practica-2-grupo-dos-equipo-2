"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from src.gestorAplicacion.serviciosOfrecidos.Consulta import Consulta
from src.gestorAplicacion.instalaciones.Lugar import Lugar

# Descripción: Esta clase hereda de Consulta y representa una cirugía médica.
# Incluye información específica para las cirugías, como los resultados de los laboratorios, los resultados de la anestesia y las instrucciones especiales para el paciente.


class Cirugia(Consulta):
    # Constante específica para la clase Cirugia
    PRECIO_BASE_CIRUGIA = 1000000

    # Inicializador
    def __init__(self, nombre, especialidad, enfermedad, cita):
        super().__init__(nombre, especialidad, enfermedad, cita)
        self._resultadoLaboratorio = False
        self._resultadoAnestesia = False
        self._instruccionesEspeciales = ""
        cita.getPaciente().actualizarHistorialCirugias(self)

    # Calcula el precio de la consulta para un paciente dado.
    def calcularPrecio(self, paciente):
        categoria = paciente.getCategoria()
        lugar = Lugar.QUIROFANO
        costoBase = Cirugia.PRECIO_BASE_CIRUGIA
        costoTotal = (costoBase + lugar.getPrecio()) * \
            categoria.getCostoFactor()
        return costoTotal

    # Convierte la información de la consulta en una cadena de texto.
    def __str__(self):
        return (f"* Cirugia con el médico: {self.getCita().getMedico().getNombre()}\n"
                f"* Especialidad: {self.getCita().getMedico().getEspecialidad()}\n"
                f"* Enfermedad: {self.getEnfermedad().getNombre()}\n"
                f"* Fecha: {self.getCita().getFecha()}\n"
                f"* Precio: {self.calcularPrecio(self.getCita().getPaciente())}\n")

    # Getters y Setters
    def getResultadoLaboratorio(self):
        return self._resultadoLaboratorio

    def setResultadoLaboratorio(self, resultadoLaboratorio):
        self._resultadoLaboratorio = resultadoLaboratorio

    def getResultadoAnestesia(self):
        return self._resultadoAnestesia

    def setResultadoAnestesia(self, resultadoAnestesia):
        self._resultadoAnestesia = resultadoAnestesia

    def getInstruccionesEspeciales(self):
        return self._instruccionesEspeciales

    def setInstruccionesEspeciales(self, instruccionesEspeciales):
        self._instruccionesEspeciales = instruccionesEspeciales
