"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

# Descripción: Este enumerado representa los diferentes lugares en los que se pueden realizar tratamientos médicos dentro de Athenea OlympicCare.
# Cada lugar tiene asociado un precio específico que representa un costo adicional que se debe tener en cuenta al calcular el precio total de un tratamiento.
from enum import Enum
class Lugar(Enum):
    CONSULTORIO = 40000
    GIMNASIO = 55000
    QUIROFANO = 80000

    def getPrecio(self):
        return self.value
