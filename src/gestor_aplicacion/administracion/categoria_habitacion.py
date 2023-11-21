""" Maria Paula Ardila, Daniela Cristina Garcia Torres, Leopold Pierre Lanard
Jose Nicolas Duque Linares, Ronal Yesid Castro Romero """
from enum import Enum
# enum que contiene las categorias de las habitaciones y sus precios


class Categoria_habitacion(Enum):
    CAMILLA = 50000
    INDIVIDUAL = 150000
    DOBLE = 320000
    OBSERVACION = 500000
    UCI = 1300000
    UCC = 1500000

    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor
