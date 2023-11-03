"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""
import sys

# Descripción: Clase Banco que gestiona las transferencias, créditos y donaciones entre pacientes y hospitales.

max_float = sys.float_info.max
class Banco:
    
    def __init__(self):
        # Establece la caja fuerte con el valor máximo de float
        self._cajaFuerte = max_float

    # Realiza una transferencia desde el paciente al hospital, si el monto es positivo y el saldo del paciente es suficiente.
    def transferencia(self, paciente, hospital, monto):
        if monto > 0 and paciente.getCuentaBancaria().getSaldo() >= monto:
            # Realiza el débito en la cuenta del paciente
            paciente.getCuentaBancaria().debitar(monto)
    
            # Realiza el depósito en la cuenta del hospital
            hospital.getCuentaBancaria().depositar(monto)

    # Deposita un monto específico en la cuenta del hospital.
    def transferencia(self, hospital, monto):
        hospital.getCuentaBancaria().depositar(monto)

    # El paciente pide un crédito al banco. El banco resta el dinero necesario de su caja fuerte y lo añade como deuda en la cuenta bancaria del paciente.
    def pedirCredito(self, paciente, hospital, dineroNecesario, costoTotalConIVA):
        self._cajaFuerte -= dineroNecesario
        paciente.getCuentaBancaria().agregarDeuda(dineroNecesario)
        saldoRestar = paciente.getCuentaBancaria().getSaldo()
        paciente.getCuentaBancaria().debitar(saldoRestar)
        self.transferencia(hospital, costoTotalConIVA)
        paciente.marcarServiciosComoPagados()

    # Calcula el dinero total de las donaciones de órganos del paciente.
    def calcularDineroDonacion(self, paciente):
        donacionesPaciente = paciente.getCuentaBancaria().getOrganosDonar()
        montoTotalDonacion = 0
        
        # Recorre el diccionario de donaciones del paciente
        for organo, cantidadDonada in donacionesPaciente.items():
            precioOrgano = organo.getPrecio()
            montoDonadoPorOrgano = cantidadDonada * precioOrgano
            
            # Agrega el monto donado por el órgano al monto total de donación
            montoTotalDonacion += montoDonadoPorOrgano
        
        return montoTotalDonacion

    # Procesa la donación de órganos del paciente, calculando el monto total y gestionando las transferencias correspondientes.
    def donacion(self, paciente, hospital, costoTotalConIVA):
        dineroTotalDonacion = self.calcularDineroDonacion(paciente)
        diferencia = dineroTotalDonacion - costoTotalConIVA
        
        if diferencia >= 0:
            self.transferencia(hospital, costoTotalConIVA)
            paciente.marcarServiciosComoPagados()
            paciente.getCuentaBancaria().depositar(diferencia)
        else:
            dineroRestante = -1 * diferencia
            self._cajaFuerte -= dineroRestante
            regaloSolidario = dineroRestante
            self.transferencia(hospital, regaloSolidario)
            paciente.marcarServiciosComoPagados()

    # Getters y Setters
    def getCajaFuerte(self):
        return self._cajaFuerte

    def setCajaFuerte(self, cajaFuerte):
        self._cajaFuerte = cajaFuerte

