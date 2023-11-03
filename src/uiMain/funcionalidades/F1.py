"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""
from gestorAplicacion.sujeto import Paciente, Medico, Categoria, Especialidad, ListaProfesionales
from gestorAplicacion.adminHospitalaria import Hospital
from gestorAplicacion.instalaciones import Fecha
from gestorAplicacion.serviciosOfrecidos import Tipo
from uiMain import Screen
from uiMain.F0 import obtenerEnumPorInput, obtenerEnteroConLimitePorInput
from datetime import datetime

class F1:

    # EL HOSPITALXD
    TESTNOMBRE = "testNombre"
    TESTDIRECCION = "testDireccion"
    HOSPITAL = Hospital(TESTNOMBRE, TESTDIRECCION)
    SCANNER_CITA = Screen.SCANNER

    @staticmethod
    def generarCita(paciente):

        # Se solicita la información de la especialidad para la que se desea tener cita.
        tipo = obtenerEnumPorInput(Tipo, "Ingrese el tipo de cita deseada (CONSULTA, CIRUGIA, TERAPIA): ")

        especialidad = obtenerEnumPorInput(Especialidad, "Ingrese la especialidad (ORTOPEDISTA, FISIOTERAPEUTA, NUTRICIONISTA, OPTOMETRISTA): ")
        categoria = paciente.getCategoria()

        # Se pide la fecha para la cita.
        fecha = F1.obtenerFechaPorInput()

        # Se encuentra un médico disponible con la especialidad seleccionada
        medicosDisponibles = F1.generarListaMedicos(especialidad, categoria, fecha)

        # Lógica para terminar la creación de la cita, se verifica que hay médicos disponibles para asignar al paciente.
        if len(medicosDisponibles) != 0:
            for medico in medicosDisponibles:
                print(medico)

            medicoElegido = F1.obtenerMedicoPorInput()

            # Se agenda la cita
            nuevaCita = paciente.agendarCita(medicoElegido, fecha, tipo, especialidad)

            print("--------------------------------------------------")
            print("|               Hoja de Cita Médica              |")
            print("--------------------------------------------------")
            print(f"| Paciente:{paciente.getNombre()}                                  |")
            print(f"| ID:{paciente.getNumeroIdentificacion()}                                        |")
            print(f"| Categoría:{paciente.getCategoria()}                             |")
            print(f"| Especialidad:{nuevaCita.getMedico().getEspecialidad()}                      |")
            print(f"| Médico:{nuevaCita.getMedico().getNombre()}                          |")
            print(f"| Fecha:{nuevaCita.getFecha()}                               |")
            print("--------------------------------------------------")
        else:
            print("Lo sentimos, no hay médicos disponibles para la fecha seleccionada.")

    @staticmethod
    def obtenerFechaPorInput():
        fecha = None
        dia = mes = año = hora = 0
        APERTURA = 7
        CIERRE = 22
        LIMITEAÑO = 2024
        AÑOACTUAL = 2023

        # Obtener fecha actual
        now = datetime.now()
        diaActual = now.day
        mesActual = now.month
        añoActual = now.year

        while fecha is None:
            año = obtenerEnteroConLimitePorInput(AÑOACTUAL, LIMITEAÑO, "Ingrese el año deseado para la cita:")
            mes = obtenerEnteroConLimitePorInput(1, 12, "Ingrese el mes deseado para la cita:")

            if mes in [1, 3, 4, 7, 8, 10, 12]:
                dia = obtenerEnteroConLimitePorInput(1, 31, "Ingrese el día deseado para la cita (de 1 a 31):")
            elif mes in [5, 6, 9, 11]:
                dia = obtenerEnteroConLimitePorInput(1, 30, "Ingrese el día deseado para la cita (de 1 a 30):")
            else:
                dia = obtenerEnteroConLimitePorInput(1, 28, "Ingrese el día deseado para la cita (de 1 a 28) :")

            hora = obtenerEnteroConLimitePorInput(APERTURA, CIERRE, f"Ingrese la hora deseada para la cita en formato militar y sin ingresar minutos, números enteros entre {APERTURA} y {CIERRE}")

            fecha = Fecha(dia, mes, año, hora)

            if año < añoActual or (año == añoActual and mes < mesActual) or (año == añoActual and mes == mesActual and dia < diaActual):
                print("La fecha no puede ser anterior a la fecha actual. Intente de nuevo.")
                fecha = None  # Esto es para que el bucle continúe

        return fecha

    @staticmethod
    def obtenerMedicoPorInput():
        medicoObtenido = None
        ID = ''
        IDConvertido = 0

        while IDConvertido == 0:
            ID = input("Por favor ingrese el numero de identificacion del médico que desea seleccionar, sin espacios ni guiones: ")

            try:
                IDConvertido = int(ID)
            except ValueError:
                print("Entrada inválida, por favor intente de nuevo.")

        for medico in F1.HOSPITAL.getListaMedicos():
            if medico.getNumeroIdentificacion() == IDConvertido:
                medicoObtenido = medico
                return medicoObtenido

        return medicoObtenido

    @staticmethod
    def generarListaMedicos(especialidad, categoria, fecha):
        medicosDisponibles = []
        medicosPosibles = []
        medicoExcluido = None

        for medico in F1.HOSPITAL.getListaMedicos():
            if medico.getCategoria() == categoria and medico.getEspecialidad() == especialidad:
                medicosPosibles.append(medico)

        for medico in medicosPosibles:
            for cita in medico.getAgenda():
                if cita.getFecha().comparar(fecha):
                    medicoExcluido = medico

            if medicoExcluido and medicoExcluido.getNombre() != medico.getNombre():
                medicosDisponibles.append(medico)

        return medicosDisponibles