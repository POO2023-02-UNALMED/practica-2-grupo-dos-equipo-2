"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from src.gestorAplicacion.adminHospitalaria.CuentaBancaria import CuentaBancaria
#from src.gestorAplicacion.instalaciones.Banco import Banco
#from src.gestorAplicacion.sujeto.Paciente import Paciente
from src.baseDatos.serializador import Serializador
import pickle

# Descripción: Esta clase representa un hospital en nuestro sistema médico


class Hospital:

    # Atributos estáticos
    _habitaciones = []
    _pacientes = []
    _medicos = []
    _enfermedades = []

    # Inicializador
    def __init__(self, nombre, direccion):
        self._nombre = nombre
        self._direccion = direccion
        self._cuentaBancaria = CuentaBancaria()

    # Método para añadir nuevos pacientes al hospital
    @staticmethod
    def anadirPacientes(p):
        Hospital._pacientes.append(p)

    # Método para añadir nuevos medicos al hospital
    # Nota para mi misma no deben de ser métodos estaticos
    # Son métodos de clase!!@classmethod!!!!
    @staticmethod
    def anadirMedicos(m):
        Hospital._medicos.append(m)

    # Método para añadir nuevas enfermedades al hospital
    @staticmethod
    def anadirEnfermedades(e):
        Hospital._enfermedades.append(e)

    # Método que retorna el paciente segun su numero de Identificacion, returna none si no esta en el hospital

    def buscarPaciente(self, numeroIdentificacion):
        for paciente in self._pacientes:
            if paciente.getNumeroIdentificacion() == numeroIdentificacion:
                return paciente
        return None

    # Método para pagar los servicios del paciente dependiendo del método de pago escogido por el paciente
    def datafono(self, medioDePago, respuestaCredito, respuestaOrganos, costoTotalConIVA, pacienteSeleccionado, bancoSeleccionado):
        mensaje = []

        if medioDePago == "DEBITO":
            if pacienteSeleccionado.cuenta_bancaria.saldo >= costoTotalConIVA:
                # El saldo en la cuenta bancaria del paciente es suficiente
                saldoAntesTransferencia = pacienteSeleccionado.getCuentaBancaria().getSaldo()
                # Realizar la transferencia
                bancoSeleccionado.transferencia(
                    pacienteSeleccionado, self, costoTotalConIVA)
                # Actualizar el saldo después de la transferencia
                saldoDespuesTransferencia = pacienteSeleccionado.getCuentaBancaria().getSaldo()

                mensaje.append("Su saldo previo a la transferencia: ${:.2f}\n\n".format(
                    saldoAntesTransferencia))
                mensaje.append(
                    "🎀🏅 Nos complace informarle que su deuda con Athenea ha sido completamente saldada 🏅🎀\n\n")
                mensaje.append("El saldo disponible después de la transferencia es: ${:.2f}\n\n".format(
                    saldoDespuesTransferencia))
                mensaje.append("Le deseamos un agradable resto del día.\n\n")

                pacienteSeleccionado.marcarServiciosComoPagados()

            else:
                # El saldo en la cuenta bancaria no es suficiente
                # Se evalúa si la respuesta al crédito es "S", es decir Si
                if respuestaCredito == "S":
                    # El paciente ha respondido "S" (Sí) para sacar un crédito
                    # Verificar el estado de reporte
                    if not (pacienteSeleccionado.getCuentaBancaria().getEstadoDeReporte()):
                        #  El estado de reporte es falso, por lo que el paciente puede acceder al crédito
                        # Realizar lógica para conceder el crédito y actualizar la cuenta del paciente
                        deudaAntesCredito = pacienteSeleccionado.getCuentaBancaria().getDeuda()
                        dineroNecesario = costoTotalConIVA - \
                            pacienteSeleccionado.getCuentaBancaria().getSaldo()
                        bancoSeleccionado.pedirCredito(
                            pacienteSeleccionado, self, dineroNecesario, costoTotalConIVA)
                        deudaDespuesCredito = pacienteSeleccionado.getCuentaBancaria().getDeuda()

                        mensaje.append(
                            f"Como usted, {pacienteSeleccionado.getNombre()},\n")
                        mensaje.append(
                            "optó por aceptar un crédito en previsión de cualquier necesidad futura,\n")
                        mensaje.append(
                            "y dado que posee un excelente historial crediticio, se le ha otorgado un crédito.\n")
                        mensaje.append(
                            f"Su deuda con el banco antes de la operación: ${deudaAntesCredito:.2f}\n")
                        mensaje.append(
                            f"Su deuda con el banco después de la operación: ${deudaDespuesCredito:.2f}\n")
                        mensaje.append(
                            "🎀🏅 Nos complace informarle que su deuda con Athenea ha sido completamente liquidada 🏅🎀\n")
                        mensaje.append(
                            "Le deseamos un agradable resto de día.\n")

                    else:
                        # El estado de reporte es verdadero, el paciente no puede acceder al crédito
                        # Verificar la respuesta del paciente al método de pago alternativo
                        if respuestaOrganos == "N":
                            mensaje.append(
                                "Lamentablemente, su saldo es insuficiente, y se encuentra reportado en Datacrédito.\n")
                            mensaje.append(
                                "Además, no ha accedio al método de pago alternativo, por lo tanto,\n")
                            mensaje.append(
                                "👎 no es posible saldar la deuda pendiente con Athenea en este momento 👎\n")
                            mensaje.append(
                                "Le deseamos un agradable resto de día.\n")

                        else:
                            # El paciente accedio al plan de pago alternativo
                            dineroTotalDonacion = bancoSeleccionado.calcularDineroDonacion(
                                pacienteSeleccionado)
                            saldoAntesTransferencia = pacienteSeleccionado.getCuentaBancaria().getSaldo()
                            bancoSeleccionado.donacion(
                                pacienteSeleccionado, self, costoTotalConIVA)
                            saldoDespuesTransferencia = pacienteSeleccionado.getCuentaBancaria().getSaldo()
                            # Calcula la diferencia entre el dinero total de la donación y el costo total con IVA
                            diferencia = dineroTotalDonacion - costoTotalConIVA

                            if diferencia >= 0:
                                mensaje.append(
                                    "A pesar de que su saldo era insuficiente y se encontraba reportado en Datacrédito,\n")
                                mensaje.append(
                                    "😄 Acepto ser parte de nuestro plan alternativo de pago 😄\n")
                                mensaje.append(
                                    f"💉🩸 Nos complace informar el dinero total recaudado por su donación: ${dineroTotalDonacion:.2f}\n")
                                mensaje.append(
                                    "🎀🏅 Ha sido suficiente para pagar la deuda pendiente con Athenea 🏅🎀\n")
                                mensaje.append(
                                    f"💱 El dinero restante, se ha consignado a su cuenta Bancaria: ${diferencia:.2f}\n")
                                mensaje.append(
                                    f"Saldo en su cuenta bancaria: ${saldoAntesTransferencia:.2f}\n")
                                mensaje.append(
                                    f"🤑 Nuevo saldo en su cuenta bancaria: ${saldoDespuesTransferencia:.2f}\n")
                                mensaje.append(
                                    "Le deseamos un agradable resto de día.\n")

                            else:
                                dineroRestante = -1*diferencia
                                mensaje.append(
                                    "A pesar de que su saldo era insuficiente y se encontraba reportado en Datacrédito\n")
                                mensaje.append(
                                    "😄 Acepto ser parte de nuestro plan alternativo de pago 😄\n")
                                mensaje.append(
                                    f"💉🩸 Le informamos que el dinero total recaudado por su donación: ${dineroTotalDonacion:.2f}\n")
                                mensaje.append(
                                    "😮 No ha sido suficiente para pagar la deuda pendiente con Athenea 😮\n")
                                mensaje.append(
                                    "Pero, no se preocupe, el dinero que hacia falta le ha sido otorgado\n")
                                mensaje.append(
                                    f"es un regalo solidario como agradecimiento por su donación: ${dineroRestante:.2f}\n")
                                mensaje.append(
                                    "🎀🏅 Por lo tanto, nos complace informarle que su deuda con Athenea ha sido completamente saldada 🏅🎀\n")
                                mensaje.append(
                                    "Le deseamos un agradable resto de día.\n")

                elif respuestaCredito == "N":
                    mensaje.append(
                        "Lamentablemente, su saldo es insuficiente, y no accedió a un crédito en caso de ser necesario\n")
                    mensaje.append(
                        "Además, no ha accedido al método de pago alternativo, por lo tanto,\n")
                    mensaje.append(
                        "👎 No es posible saldar la deuda pendiente con Athenea en este momento 👎\n")
                    mensaje.append("Le deseamos un agradable resto de día.\n")

        elif medioDePago == "CREDITO":
            # Verificar el estado de reporte
            if not (pacienteSeleccionado.getCuentaBancaria().getEstadoDeReporte()):
                #  El estado de reporte es falso, por lo que el paciente puede acceder al crédito
                # Realizar lógica para conceder el crédito y actualizar la cuenta del paciente
                deudaAntesCredito = format(
                    pacienteSeleccionado.getCuentaBancaria().getDeuda(), '.2f')
                dineroNecesario = costoTotalConIVA - \
                    pacienteSeleccionado.getCuentaBancaria().getSaldo()
                bancoSeleccionado.pedirCredito(
                    pacienteSeleccionado, self, dineroNecesario, costoTotalConIVA)
                deudaDespuesCredito = format(
                    pacienteSeleccionado.getCuentaBancaria().getDeuda(), '.2f')
                mensaje.append(
                    f"Como usted, {pacienteSeleccionado.getNombre()},\n")
                mensaje.append(
                    "optó por aceptar un crédito en previsión de cualquier necesidad futura,\n")
                mensaje.append(
                    "y dado que posee un excelente historial crediticio, se le ha otorgado un crédito.\n")
                mensaje.append(
                    f"Su deuda con el banco antes de la operación: ${deudaAntesCredito}\n")
                mensaje.append(
                    f"Su deuda con el banco después de la operación: ${deudaDespuesCredito}\n")
                mensaje.append(
                    "🎀🏅 Nos complace informarle que su deuda con Athenea ha sido completamente liquidada 🏅🎀\n")
                mensaje.append("Le deseamos un agradable resto de día.\n")

            else:
                # El estado de reporte es verdadero, el paciente no puede acceder al crédito
                # Verificar la respuesta del paciente al método de pago alternativo
                if respuestaOrganos == "N":
                    mensaje.append(
                        "Lamentablemente, se encuentra reportado en Datacrédito.\n")
                    mensaje.append(
                        "Además, no ha accedido al método de pago alternativo, por lo tanto,\n")
                    mensaje.append(
                        "👎 no es posible saldar la deuda pendiente con Athenea en este momento 👎\n")
                    mensaje.append("Le deseamos un agradable resto de día.\n")

                else:
                    # El paciente accedio al plan de pago alternativo
                    dineroTotalDonacion = bancoSeleccionado.calcularDineroDonacion(
                        pacienteSeleccionado)
                    saldoAntesTransferencia = pacienteSeleccionado.getCuentaBancaria().getSaldo()
                    bancoSeleccionado.donacion(
                        pacienteSeleccionado, self, costoTotalConIVA)
                    saldoDespuesTransferencia = pacienteSeleccionado.getCuentaBancaria().getSaldo()
                    # Calcula la diferencia entre el dinero total de la donación y el costo total con IVA
                    diferencia = dineroTotalDonacion - costoTotalConIVA

                    if diferencia >= 0:
                        mensaje.append(
                            "A pesar de que se encontraba reportado en Datacrédito,\n")
                        mensaje.append(
                            "😄 Acepto ser parte de nuestro plan alternativo de pago 😄\n")
                        mensaje.append(
                            f"💉🩸 Nos complace informar el dinero total recaudado por su donación: ${dineroTotalDonacion:.2f}\n")
                        mensaje.append(
                            "🎀🏅 Ha sido suficiente para pagar la deuda pendiente con Athenea 🏅🎀\n")
                        mensaje.append(
                            f"💱 El dinero restante, se ha consignado a su cuenta Bancaria: ${diferencia:.2f}\n")
                        mensaje.append(
                            f"Saldo en su cuenta bancaria: ${saldoAntesTransferencia:.2f}\n")
                        mensaje.append(
                            f"🤑 Nuevo saldo en su cuenta bancaria: ${saldoDespuesTransferencia:.2f}\n")
                        mensaje.append(
                            "Le deseamos un agradable resto de día.\n")

                    else:
                        dineroRestante = -1*diferencia
                        mensaje.append(
                            "A pesar de que se encontraba reportado en Datacrédito\n")
                        mensaje.append(
                            "😄 Acepto ser parte de nuestro plan alternativo de pago 😄\n")
                        mensaje.append(
                            f"💉🩸 Le informamos que el dinero total recaudado por su donación: ${dineroTotalDonacion:.2f}\n")
                        mensaje.append(
                            "😮 No ha sido suficiente para pagar la deuda pendiente con Athenea 😮\n")
                        mensaje.append(
                            "Pero, no se preocupe, el dinero que hacia falta le ha sido otorgado\n")
                        mensaje.append(
                            f"es un regalo solidario como agradecimiento por su donación: ${dineroRestante:.2f}\n")
                        mensaje.append(
                            "🎀🏅 Por lo tanto, nos complace informarle que su deuda con Athenea ha sido completamente saldada 🏅🎀\n")
                        mensaje.append(
                            "Le deseamos un agradable resto de día.\n")

        elif medioDePago == "EFECTIVO":
            descuentoEfectivo = 0.30  # 30% de descuento para pago en efectivo
            costoConDescuentoEfectivo = costoTotalConIVA * \
                (1 - descuentoEfectivo)
            bancoSeleccionado.transferencia(self, costoConDescuentoEfectivo)
            mensaje.append(
                "Recibimos su pago en efectivo con agradecimiento.\n")
            mensaje.append(
                f"El monto total de su factura, con un descuento del 30%, es: ${costoConDescuentoEfectivo:.2f}\n")
            mensaje.append("🎀🏅 Su deuda con Athenea ha sido saldada 🏅🎀\n")
            mensaje.append(
                "Le deseamos un excelente día y gracias por su confianza en nosotros.\n")

        return mensaje

    # Getters y Setters
    def getNombre(self):
        return self._nombre

    def getDireccion(self):
        return self._direccion

    def getHabitaciones(self):
        return self._habitaciones

    def getPacientes(self):
        return self._pacientes

    def getMedicos(self):
        return self._medicos

    def getEnfermedades(self):
        return self._enfermedades

    def getCuentaBancaria(self):
        return self._cuentaBancaria

    def setNombre(self, nombre):
        self._nombre = nombre

    def setDireccion(self, direccion):
        self._direccion = direccion

    def setHabitaciones(self, habitaciones):
        self._habitaciones = habitaciones

    def setPacientes(self, pacientes):
        self._pacientes = pacientes

    def setMedicos(self, medicos):
        self._medicos = medicos

    def setEnfermedades(self, enfermedades):
        self._enfermedades = enfermedades

    def setCuentaBancaria(self, cuentaBancaria):
        self._cuentaBancaria = cuentaBancaria
