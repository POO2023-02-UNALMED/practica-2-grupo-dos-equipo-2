from excepciones.ErrorAplicacion import ErrorAplicacion


class ErrorAsignacion(ErrorAplicacion):
    
    def __init__(self, mensaje):
        self.mensaje_error_asigancion = f" Error de existencia: {mensaje}"
        super().__init__(self.mensaje_error_asigancion)

class Excepcion_1(ErrorAsignacion):

    def __init__(self, id):
        self.mensaje_error = f"\nEl paciente con ID {id}  debe un servicio"
        super().__init__(self.mensaje_error)

class Excepcion_2(ErrorAsignacion):
    
    def __init__(self, id):
        self.mensaje_error = f"\nEl medico con ID {id} no tiene agenda disponible para citas"
        super().__init__(self.mensaje_error)

class Excepcion_3(ErrorAsignacion):

     def __init__(self, id):
         self.mensaje_error = f"\nNo existe un paciente con el ID: {id}"
         super().__init__(self.mensaje_error)

class Excepcion_4(ErrorAsignacion):

    def __init__(self, id):
        self.mensaje_error = f"\nNo existe un medico con el ID: {id}"
        super().__init__(self.mensaje_error)