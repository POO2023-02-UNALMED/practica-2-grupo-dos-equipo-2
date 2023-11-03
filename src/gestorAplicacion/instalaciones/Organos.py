"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from enum import Enum

# Descripción: Este enumerado representa diferentes tipos de órganos y su respectivo precio.
class Organos(Enum):
    OJO = 750000
    OREJA = 950000
    PORCION_DE_HIGADO = 1235000
    RIÑON = 1950000
    UNA_EXTREMIDAD_SUPERIOR = 2450000
    UNA_EXTREMIDAD_INFERIOR = 3000000

    def getPrecio(self):
        return self.value
