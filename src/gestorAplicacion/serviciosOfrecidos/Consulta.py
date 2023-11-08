"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from src.gestorAplicacion.serviciosOfrecidos.Tratamiento import Tratamiento
from src.gestorAplicacion.instalaciones.Lugar import Lugar
from src.gestorAplicacion.sujeto.Paciente import Paciente
from src.gestorAplicacion.sujeto.Categoria import Categoria

# Descripción: La clase Consulta representa un tipo específico de tratamiento médico que se realiza en un consultorio.


class Consulta (Tratamiento):
    # Constante específica para la clase Consulta
    PRECIO_BASE_CONSULTA = 600000

    # Inicializador
    def __init__(self, nombre, especialidad, enfermedad, cita):
        super().__init__(nombre, especialidad, enfermedad, cita)
        cita.getPaciente().actualizarHistorialEnfermedades(enfermedad)

    # Calcula el precio de la consulta para un paciente dado.
    def calcularPrecio(paciente):
        categoria = paciente.getCategoria()
        lugar = Lugar.CONSULTORIO
        costoBase = Consulta.PRECIO_BASE_CONSULTA
        costoTotal = (costoBase + lugar.getPrecio()) * \
            categoria.getCostoFactor()
        return costoTotal

    # Convierte la información de la consulta en una cadena de texto.
    def __str__(self):
        return (f"* Consulta con el médico: {self.getCita().getMedico().getNombre()}\n"
                f"* Especialidad: {self.getCita().getMedico().getEspecialidad()}\n"
                f"* Enfermedad: {self.getEnfermedad().getNombre()}\n"
                f"* Fecha: {self.getCita().getFecha()}\n"
                f"* Precio: {self.calcularPrecio(self.getCita().getPaciente())}\n")
