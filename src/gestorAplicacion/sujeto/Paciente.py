"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""

from src.gestorAplicacion.instalaciones.Hospital import Hospital
from src.gestorAplicacion.sujeto.Persona import Persona
from src.gestorAplicacion.adminHospitalaria.Cita import Cita
from src.gestorAplicacion.adminHospitalaria.Pago import Pago
from src.gestorAplicacion.adminHospitalaria.HistoriaClinica import HistoriaClinica
from src.gestorAplicacion.adminHospitalaria.CuentaBancaria import CuentaBancaria


# Descripción: Representa a un Paciente dentro del sistema de salud.


class Paciente(Persona, Pago):

    # Inicializador
    def __init__(self, categoria, numeroIdentificacion, nombre, sexo, peso, talla):
        super().__init__(categoria, numeroIdentificacion, nombre)
        self._historiaClinica = HistoriaClinica(self)
        self._cuentaBancaria = CuentaBancaria()
        self._sexo = sexo
        self._peso = peso
        self._talla = talla
        self._serviciosSinPagar = []
        self._serviciosSeleccionados = []
        self._ultimaCita = []
        Hospital.anadirPacientes(self)
        # Nota: A la persona que usaba los atributos citas y consultas, por favor use los atributos que se encuentran en historia clinica que representan esto mismo.

    # Implementación del método obtenerServiciosSinPagar de la clase abstracta Pago
    def obtenerServiciosSinPagar(self):
        infoServiciosSinPagar = []
        indicesDisponibles = []

        # Limpiar la lista en caso de llamadas múltiples
        self._serviciosSinPagar.clear()

        # Recorre las consultas sin pagar y agrega al listado de servicios sin pagar
        for consulta in self._historiaClinica.getHistorialConsultas():
            if not consulta.isPagada():
                self._serviciosSinPagar.append(consulta)

        # Recorre las cirugias sin pagar y agrega al listado de servicios sin pagar
        for cirugia in self._historiaClinica.getHistorialCirugias():
            if not cirugia.isPagada():
                self._serviciosSinPagar.append(cirugia)

        # Recorre las terapias sin pagar y agrega al listado de servicios sin pagar
        for terapia in self._historiaClinica.getHistorialTerapias():
            if not terapia.isPagada():
                self._serviciosSinPagar.append(terapia)

        # Verifica si hay servicios sin pagar
        if self._serviciosSinPagar:
            infoServiciosSinPagar.append(
                f"Total de servicios sin Pagar: {len(self._serviciosSinPagar)}\n")

            # Recorre la lista de servicios sin pagar y agrega la información a la lista
            for i, servicio in enumerate(self._serviciosSinPagar):
                infoServiciosSinPagar.append(f"Servicio N° {i}\n")
                infoServiciosSinPagar.append(str(servicio) + "\n")
                indicesDisponibles.append(str(i))
        else:
            return ["No hay servicios pendientes de pago"]

        return [' '.join(infoServiciosSinPagar), ' '.join(indicesDisponibles)]

    """ 
    Este método permite al paciente seleccionar servicios pendientes de pago especificando los índices correspondientes.
    Calcula el costo total de los servicios seleccionados, aplicando descuentos si corresponde.
    Además, calcula el costo total con IVA incluido y retorna estos tres costos en un arreglo.
    Si no se selecciona ningún servicio, el costo total y el costo total con descuento serán iguales.
    """

    def seleccionarServiciosAPagar(self, indices):
        # Divide la cadena de índices en una lista de strings
        indicesArray = indices.split(",")

        # Inicializa el costo total en 0.0
        costoTotal = 0.0

        # Limpia los servicios seleccionados antes de agregar los nuevos
        self.serviciosSeleccionados.clear()

        # Recorre los índices especificados por el usuario
        for indiceStr in indicesArray:
            # Convierte el índice en un número entero
            indice = int(indiceStr)

            # Verifica que el índice esté dentro del rango de serviciosSinPagar
            if indice >= 0 and indice < len(self.serviciosSinPagar):
                # Obtiene el servicio correspondiente al índice
                servicio = self.serviciosSinPagar[indice]

                # Agrega el servicio seleccionado a serviciosSeleccionados
                self.serviciosSeleccionados.append(servicio)

                # Calcula el costo del servicio y lo agrega al costo total
                costoServicio = servicio.calcularPrecio(self)
                costoTotal += costoServicio

        # Aplica descuento si se cumplen ciertas condiciones
        if len(indicesArray) >= 5:
            descuento = 0.0
            if len(indicesArray) >= 20:
                descuento = 0.5  # Descuento del 50% para 20 o más servicios
            elif len(indicesArray) >= 15:
                descuento = 0.4  # Descuento del 40% para 15 o más servicios
            elif len(indicesArray) >= 10:
                descuento = 0.3  # Descuento del 30% para 10 o más servicios
            elif len(indicesArray) >= 5:
                descuento = 0.2  # Descuento del 20% para 5 o más servicios

            # Aplica el descuento al costo total
            costoTotalConDescuento = costoTotal - costoTotal * descuento

            # Calcula el costo total con IVA incluido usando el método de la clase Pago
            costoTotalConIVA = self.calcularTotalConIVA(costoTotalConDescuento)

            # Retorna los tres costos
            return [costoTotal, costoTotalConDescuento, costoTotalConIVA]
        else:
            # No se aplica descuento, por lo que el costo total con descuento es igual al costo total
            # Calcula el costo total con IVA incluido usando el método de la clase Pago
            costoTotalConIVA = self.calcularTotalConIVA(costoTotal)
            return [costoTotal, costoTotal, costoTotalConIVA]

    # Método encargado de modificar el estado de pago de los métodos seleccionados
    def marcarServiciosComoPagados(self):
        for servicio in self.serviciosSeleccionados:
            servicio.marcarComoPagada()

    def agendarCita(self, medico, fecha, tipo, especialidad):
        nuevaCita = Cita(medico, fecha, self, tipo,
                         especialidad, self._categoria)
        self.actualizarHistorialCitas(nuevaCita)
        return nuevaCita

    # Métodos para actualizar la historia clinica
    def actualizarHistorialEnfermedades(self, nuevaEnfermedad):
        self._historiaClinica.getHistorialEnfermedades().append(nuevaEnfermedad)

    def actualizarHistorialOrdenes(self, nuevaOrden):
        self._historiaClinica.getHistorialOrdenes().append(nuevaOrden)

    def actualizarHistorialTerapias(self, nuevaTerapia):
        self._historiaClinica.getHistorialTerapias().append(nuevaTerapia)

    def actualizarHistorialCirugias(self, nuevaCirugia):
        self._historiaClinica.getHistorialCirugias().append(nuevaCirugia)

    def actualizarHistorialConsultas(self, nuevaConsulta):
        self._historiaClinica.getHistorialConsultas().append(nuevaConsulta)

    def actualizarHistorialRutinas(self, nuevaRutina):
        self._historiaClinica.getHistorialRutinas().append(nuevaRutina)

    def actualizarHistorialCitas(self, nuevaCita):
        self._historiaClinica.getHistorialCitas().append(nuevaCita)

    # Getters y Setters
    def getHistoriaClinica(self):
        return self._historiaClinica

    def setHistoriaClinica(self, historiaClinica):
        self._historiaClinica = historiaClinica

    def getCuentaBancaria(self):
        return self._cuentaBancaria

    def setCuentaBancaria(self, cuentaBancaria):
        self._cuentaBancaria = cuentaBancaria

    def getSexo(self):
        return self._sexo

    def setSexo(self, sexo):
        self._sexo = sexo

    def getPeso(self):
        return self._peso

    def setPeso(self, peso):
        self._peso = peso

    def getTalla(self):
        return self._talla

    def setTalla(self, talla):
        self._talla = talla

    def getServiciosSinPagar(self):
        return self._serviciosSinPagar

    def setServiciosSinPagar(self, serviciosSinPagar):
        self._serviciosSinPagar = serviciosSinPagar

    def getServiciosSeleccionados(self):
        return self._serviciosSeleccionados

    def setServiciosSeleccionados(self, serviciosSeleccionados):
        self._serviciosSeleccionados = serviciosSeleccionados

    def getUltimaCita(self):
        if not self.citas:
            return None
        return self.citas[-1]
