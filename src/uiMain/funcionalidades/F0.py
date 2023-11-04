"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""
from src.gestorAplicacion.sujeto import Paciente
from src.uiMain.funcionalidades import F0


def screen_orden_medica():
    paciente= F0.obtener_paciente_por_input()
    cita= Paciente.getUltimaCita()
    if cita is None:
        print("el Paciente no tiene citas en el registro")
        return


def obtener_paciente_por_input():
    paciente_elegido = None
    id_elegido = 0

    while True:
        id_elegido = F0.obtener_entero_por_input("Por favor ingrese el numero de identificacion del paciente: ")
        for paciente in F0.UTILITY_HOSPITAL.get_lista_pacientes():
            if id_elegido == paciente.get_numero_identificacion():
                paciente_elegido = paciente
                return paciente_elegido
        
        if paciente_elegido is None:
            print("No hemos podido encontrar al paciente en nuestro sistema, por favor intente de nuevo.")

def obtener_entero_con_limite_por_input(limite_inferior, limite_superior, mensaje):
    entero_chequeado = None
    
    while entero_chequeado is None or entero_chequeado < limite_inferior or entero_chequeado > limite_superior:
        try:
            entero_chequeado = int(input(mensaje))
            if entero_chequeado < limite_inferior or entero_chequeado > limite_superior:
                print("Entrada inválida, por favor intente de nuevo.")
        except ValueError:
            print("Entrada inválida, por favor intente de nuevo.")
    
    return entero_chequeado
