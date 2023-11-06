"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from src.gestorAplicacion.serviciosOfrecidos.Consulta import Consulta
from src.gestorAplicacion.instalaciones.Lugar import Lugar

# Descripción: Esta clase representa una terapia, un tipo específico de consulta médica.


class Terapia(Consulta):
    # Constante específica para la clase Terapia
    PRECIO_BASE_TERAPIA = 2000000

    # Inicializador
    def __init__(self, nombre, especialidad, enfermedad, cita):
        super().__init__(nombre, especialidad, enfermedad, cita)
        cita.getPaciente().actualizarHistorialTerapias(self)

    # Calcula el precio de la terapia para un paciente dado.
    def calcularPrecio(self, paciente):
        categoria = paciente.getCategoria()
        lugar = Lugar.GIMNASIO
        costoBase = self.PRECIO_BASE_TERAPIA
        costoTotal = (costoBase + lugar.value.precio) * \
            categoria.getCostoFactor()
        return costoTotal

    # Convierte la información de la terapia en una cadena de texto.
    def __str__(self):
        return (f"* Terapia con el médico: {self.getCita().getMedico().getNombre()}\n" +
                f"* Especialidad: {self.getCita().getMedico().getEspecialidad().name}\n" +
                f"* Enfermedad: {self.getEnfermedad().getNombre()}\n" +
                f"* Fecha: {self.getCita().getFecha()}\n" +
                f"* Precio: {self.calcularPrecio(self.getCita().getPaciente())}\n")
