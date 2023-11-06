"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""


from enum import Enum

# Descripción: Este enumerado representa las distintas categorías de sujetos en el sistema, con un factor de costo asociado a cada categoría.


class Categoria(Enum):
    ALTO_RENDIMIENTO = 1.5
    OLIMPICO = 0.8
    AFICIONADOS = 0.7

    def getCostoFactor(self):
        return self.value
