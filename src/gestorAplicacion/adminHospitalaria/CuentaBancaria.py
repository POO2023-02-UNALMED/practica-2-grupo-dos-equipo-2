"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from src.gestorAplicacion.instalaciones.Organos import Organos
import random

# Descripción: Esta clase representa una cuenta bancaria con funcionalidades específicas,
# como saldo, deuda, estado de reporte y la capacidad de donar órganos.

class CuentaBancaria:

    # Inicializador
    def __init__(self):
        self._saldo = self.generadorSaldoAleatorio()
        self._deuda = 0.0
        self._estadoDeReporte = self.generarEstadoDeReporteAleatorio()
        self._organosDonar = {}

    # Este método debita un monto especificado del saldo de la cuenta.
    def debitar(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto

    # Este método deposita un monto especificado al saldo de la cuenta.
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto

    # Este método agrega una cantidad especificada a la deuda actual.
    def agregarDeuda(self, cantidad):
        self._deuda += cantidad

    # Este método agrega o actualiza un órgano a donar y su respectiva cantidad.
    def agregarOrganoDonar(self, organo, cantidad):
        # Verificar si el órgano ya existe en el diccionario
        if organo in self._organosDonar:
            # Si existe, actualizar la cantidad
            self._organosDonar[organo] += cantidad
        else:
            # Si no existe, agregarlo al diccionario
            self._organosDonar[organo] = cantidad

    # Genera aleatoriamente un estado de reporte (True o False).
    def generarEstadoDeReporteAleatorio(self):
        # Genera un valor aleatorio
        return random.choice([True, False])

    # Genera aleatoriamente un saldo dentro de un rango determinado.
    def generadorSaldoAleatorio(self):
        # Define los límites del rango
        saldoMinimo = 500000.0
        saldoMaximo = 6000000.0
        # Genera un valor aleatorio dentro del rango
        saldoAleatorio = saldoMinimo + \
            (saldoMaximo - saldoMinimo) * random.random()
        return saldoAleatorio

    # Getters y Setters
    def getSaldo(self):
        return self._saldo

    def setSaldo(self, saldo):
        self._saldo = saldo

    def getOrganosDonar(self):
        return self._organosDonar

    def setOrganosDonar(self, organosDonar):
        self._organosDonar = organosDonar

    def getEstadoDeReporte(self):
        return self._estadoDeReporte

    def setEstadoDeReporte(self, estadoDeReporte):
        self._estadoDeReporte = estadoDeReporte

    def getDeuda(self):
        return self._deuda

    def setDeuda(self, deuda):
        self._deuda = deuda
