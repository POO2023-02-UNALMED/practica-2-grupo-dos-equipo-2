"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

# Descripción: La clase Tipo es una enumeración que se utiliza para definir y categorizar los diferentes tipos
# de servicios médicos que se pueden ofrecer en una clínica u hospital
from enum import Enum


class Tipo(Enum):
    # Los valores enteros 1, 2 y 3 se asignan para darles un valor único a cada
    # miembro de la enumeración, sin embargo, no son importantes, pueden ser cualquier
    CONSULTA = 1
    CIRUGIA = 2
    TERAPIA = 3
