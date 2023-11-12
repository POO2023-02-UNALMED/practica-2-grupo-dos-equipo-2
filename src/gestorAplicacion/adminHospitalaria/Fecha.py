from datetime import datetime

class Fecha:
    def __init__(self, dia, mes, año, hora):
        self.dia = dia
        self.mes = mes
        self.año = año
        self.hora = hora
        self.fecha = None

    def __str__(self):
        return f"{self.convertir_str(self.hora)}-{self.convertir_str(self.dia)}-{self.convertir_str(self.mes)}-{self.convertir_str(self.año)}"

    def convertir_str(self, num):
        return str(num)

    def comparar(self, otra_fecha):
        return self.dia == otra_fecha.dia and self.mes == otra_fecha.mes and self.año == otra_fecha.año

    def formatear_fecha(self):
        fecha_para_formatear = f"{self.hora}/{self.dia}/{self.mes}/{self.año}"
        formato = "%H/%d/%m/%Y"
        fecha_formateada = datetime.strptime(fecha_para_formatear, formato)
        self.fecha = fecha_formateada
        return fecha_formateada

    @staticmethod
    def obtener_fecha_actual():
        fecha_actual = datetime.now()
        return fecha_actual