"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

# Descripción: Esta clase abstracta representa un conjunto de métodos y constantes relacionados con el cálculo de pagos.
class Pago():
    IVA = 0.19  # 19% de IVA

    @staticmethod
    def _valorIncluidoIVA(total):
        return total + (total * Pago.IVA)

    def calcularTotalConIVA(self, total):
        return self._valorIncluidoIVA(total)


    def obtenerServiciosSinPagar(self):
        pass