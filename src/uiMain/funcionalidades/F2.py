"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""


from src.gestorAplicacion.sujeto import Medico
from src.gestorAplicacion.adminHospitalaria import Categoria, OrdenMedica
from src.gestorAplicacion.sujeto import Especialidad
from src.gestorAplicacion.serviciosOfrecidos.recursosDeTerapia import Restriccion

imput = input  # En Python no necesitamos un objeto Scanner, podemos usar `input` directamente.

# Método para asignar el médico
def asignarMedico():
    print("Asigne el meedico que atendera al paciente: ")
    ortopedista = Medico(Categoria.ALTO_RENDIMIENTO, 78964, "Dr. Pérez", Especialidad.ORTOPEDISTA)
    fisioterapeuta = Medico(Categoria.OLIMPICO, 789013, "Dr. Pepe", Especialidad.FISIOTERAPEUTA)
    nutricionista = Medico(Categoria.AFICIONADOS, 789014, "Dra. Molly", Especialidad.NUTRICIONISTA)
    optometrista = Medico(Categoria.OLIMPICO, 789015, "Dra. Margarita", Especialidad.OPTOMETRISTA)

    especialidadSeleccionada = obtenerEspecialidad()

    if especialidadSeleccionada == Especialidad.ORTOPEDISTA:
        medico = ortopedista
    elif especialidadSeleccionada == Especialidad.NUTRICIONISTA:
        medico = nutricionista
    elif especialidadSeleccionada == Especialidad.OPTOMETRISTA:
        medico = optometrista
    elif especialidadSeleccionada == Especialidad.FISIOTERAPEUTA:
        medico = fisioterapeuta

    return medico

# Método que nos dará la especialidad del médico
def obtenerEspecialidad():
    while True:
        print("Ingrese la especialidad -ORTOPEDISTA, FISIOTERAPEUTA, NUTRICIONISTA, OPTOMETRISTA-")
        entrada = input()

        for especialidad in Especialidad:
            if especialidad.name == entrada.upper():
                return especialidad

        print("Especialidad inválida. Por favor, ingrese una especialidad válida.")

# Este metodo se encargará de dar las restricciones que tiene el paciente
def restriccionPaciente():
    print("¿El paciente tiene alguna restricción médica? (Sí/No)")
    respuesta = input().upper()

    if respuesta == "SI":
        print("Ingrese la restricción -CARDIOVASCULAR, RESPIRATORIA, EQUILIBRIO, FUERZA, FLEXIBILIDAD-")
        restriccion = input().upper()

        try:
            return Restriccion[restriccion]
        except KeyError:
            print("Restricción no reconocida.")

    print("El paciente no tiene restricciones médicas..")
    return None

# Crearemos la orden médica
def generarOrdenMedica(ordenMedica):
    print("\033[34m==============================================================================================================\033[0m")
    print("\033[34m||                                                                                                          ||\033[0m")
    print("\033[34m||                                                                                                          ||\033[0m")
    print("\033[34m||                                             ORDEN MEDICA                                                 ||\033[0m")
    print("\033[34m||                                                                                                          ||\033[0m")
    print("\033[34m||                                                                                                          ||\033[0m")
    print("\033[34m==============================================================================================================\033[0m")
    print("\033[0;32mNombre del paciente: {}\nNúmero de identificación: {}\nSexo del paciente: {}\nPeso del paciente: {}\nTalla del paciente: {}\033[0m".format(ordenMedica.getPaciente().getNombre(), ordenMedica.getPaciente().getNumeroIdentificacion(), ordenMedica.getPaciente().getSexo(), ordenMedica.getPaciente().getPeso(), ordenMedica.getPaciente().getTalla()))
    print("\033[34m==============================================================================================================\033[0m")
    print("\033[0;32mNombre del Medico: {}\nEspecialidad: {}\nNumero de identificacion: {}\033[0m".format(ordenMedica.getMedico().getNombre(), ordenMedica.getMedico().getEspecialidad(), ordenMedica.getMedico().getNumeroIdentificacion()))
    print("\033[34m==============================================================================================================\033[0m")
    print("\033[34mEnfermedad del paciente: {}\nSintomas de la enfermedad: {}\033[0m".format(ordenMedica.getEnfermedad().getNombre(), ordenMedica.getEnfermedad().getSintomas()))
    print("\033[34m==============================================================================================================\033[0m")
    print("\033[34mRecomendaciones: {}\033[0m".format(ordenMedica.getRecomendaciones()))
    print("\033[34m==============================================================================================================\033[0m")

def screenOrdenMedica(consulta):
    paciente = consulta.getPaciente()
    enfermedad = consulta.getEnfermedad()
    medico = consulta.getMedico()
    
    recomendaciones = input("Por favor ingrese las recomendaciones, solo presione enter después de ingresar toda la información: ")

    ordenNueva = OrdenMedica(paciente, enfermedad, medico, recomendaciones)

    generarOrdenMedica(ordenNueva)
    paciente.actualizarHistorialOrdenes(ordenNueva)
