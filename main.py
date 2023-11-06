
"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""
from src.gestorAplicacion.instalaciones.Hospital import Hospital
from src.gestorAplicacion.instalaciones.Banco import Banco
from src.baseDatos.serializador import Serializador
from src.baseDatos.deserializador import Deserializador
from src.gestorAplicacion.serviciosOfrecidos.Consulta import Consulta
from src.gestorAplicacion.serviciosOfrecidos.Terapia import Terapia
from src.gestorAplicacion.serviciosOfrecidos.Tipo import Tipo
from src.gestorAplicacion.sujeto.Categoria import Categoria
from src.gestorAplicacion.sujeto.Especialidad import Especialidad
from src.gestorAplicacion.sujeto.Medico import Medico
from src.gestorAplicacion.sujeto.Paciente import Paciente
from src.gestorAplicacion.sujeto.Enfermedad import Enfermedad

if __name__ == "__main__":

    banco = Banco()
    hospital = Hospital("Athenea OlympiCare", "Cra. 65 #59a-110")

    ortopedista = Medico(Categoria.ALTO_RENDIMIENTO, 78964,
                         "Dr. Pérez", Especialidad.ORTOPEDISTA)
    fisioterapeuta = Medico(Categoria.OLIMPICO, 789013,
                            "Dr. Pepe", Especialidad.FISIOTERAPEUTA)
    nutricionista = Medico(Categoria.AFICIONADOS, 789014,
                           "Dra. Molly", Especialidad.NUTRICIONISTA)
    oftalmologa = Medico(Categoria.OLIMPICO, 789015,
                         "Dra. Margarita", Especialidad.OFTALMOLOGO)

    pacientePrueba1 = Paciente(
        Categoria.AFICIONADOS, 345, "Tartaglia", "M", 68, 179)
    pacientePrueba2 = Paciente(
        Categoria.ALTO_RENDIMIENTO, 567, "Zhongli", "M", 80, 190)
    pacientePrueba3 = Paciente(Categoria.OLIMPICO, 789, "Furina", "F", 50, 150)

    pacientePrueba3.getCuentaBancaria().setSaldo(20000)
    pacientePrueba1.getCuentaBancaria().setSaldo(10000)
    pacientePrueba1.getCuentaBancaria().setEstadoDeReporte(True)
    pacientePrueba2.getCuentaBancaria().setSaldo(0)
    pacientePrueba2.getCuentaBancaria().setEstadoDeReporte(False)

    enfermedad1 = Enfermedad("Desgarro muscular", Especialidad.FISIOTERAPEUTA,
                             "Traumatológica", "Hematomas,Dolor constante en la zona afectada", "restriccion")
    enfermedad2 = Enfermedad("DMAE", Especialidad.OFTALMOLOGO, "Oftalmológica / Genética",
                             "Visión borrosa o distorsionada en el centro del campo visual", "restriccion")
    enfermedad3 = Enfermedad("Trastorno Alimenticio", Especialidad.NUTRICIONISTA,
                             "Psicológica", "Bulimia,Anorexia nerviosa", "restriccion")
    enfermedad4 = Enfermedad("Fractura", Especialidad.ORTOPEDISTA,
                             "Traumatológica", "Dolor constante en la zona afectada", "restriccion")

    cita1 = pacientePrueba1.agendarCita(
        ortopedista, "fecha1", Tipo.CIRUGIA, Especialidad.ORTOPEDISTA)
    cita2 = pacientePrueba2.agendarCita(
        ortopedista, "fecha2", Tipo.CIRUGIA, Especialidad.ORTOPEDISTA)
    cita3 = pacientePrueba2.agendarCita(
        oftalmologa, "fecha3", Tipo.TERAPIA, Especialidad.OPTOMETRISTA)
    cita4 = pacientePrueba3.agendarCita(
        ortopedista, "fecha4", Tipo.CIRUGIA, Especialidad.ORTOPEDISTA)
    cita5 = pacientePrueba3.agendarCita(
        nutricionista, "fecha5", Tipo.CONSULTA, Especialidad.NUTRICIONISTA)
    cita6 = pacientePrueba3.agendarCita(
        fisioterapeuta, "fecha6", Tipo.CONSULTA, Especialidad.FISIOTERAPEUTA)

    cirugia1 = Cirugia("Osteosíntesis con Placas y Tornillos",
                       Especialidad.ORTOPEDISTA, enfermedad4, cita6)
    cirugia2 = Cirugia("Reducción Abierta y Fijación Interna",
                       Especialidad.ORTOPEDISTA, enfermedad4, cita1)
    cirugia3 = Cirugia("Artroplastia de Tobillo",
                       Especialidad.ORTOPEDISTA, enfermedad4, cita3)
    terapia1 = Terapia("Inyecciones anti-VEGF",
                       Especialidad.OFTALMOLOGO, enfermedad2, cita2)
    consulta1 = Consulta("Cognitivo conductual",
                         Especialidad.NUTRICIONISTA, enfermedad3, cita4)
    consulta2 = Consulta(
        "Ultrasonido", Especialidad.FISIOTERAPEUTA, enfermedad1, cita5)

    pacientePrueba3.actualizarHistorialConsultas(consulta1)
    pacientePrueba3.actualizarHistorialConsultas(consulta2)

    Serializador.guardarBanco(banco)
    Serializador.guardarHospital(hospital)
