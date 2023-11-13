"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""
from gestorAplicacion.serviciosOfrecidos.Rutina import Rutina
from gestorAplicacion.serviciosOfrecidos.Ejercicio import Ejercicio
from gestorAplicacion.serviciosOfrecidos.TipoTerapia import TipoTerapia
from gestorAplicacion.serviciosOfrecidos.TipoObjetivo import TipoObjetivo

from gestorAplicacion.instalaciones.Hospital import Hospital
from gestorAplicacion.sujeto.Paciente import Paciente
from gestorAplicacion.sujeto.Restriccion import Restriccion
from gestorAplicacion.adminHospitalaria.HistoriaClinica import HistoriaClinica

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Constantes para colores
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
PURPLE = "\033[35m"

# Utilidad para entrada de usuario
def input_scanner(prompt=''):
    return input(prompt).strip().upper()

TEST_ENFERMEDAD = None
TEST_PACIENTE = Paciente(None, 1, "asd", "asd", 1, 1)
TEST_HISTORIA_CLINICA = HistoriaClinica(TEST_PACIENTE)
TEST_PACIENTE.setHistoriaClinica(TEST_HISTORIA_CLINICA)
TEST_HOSPITAL = Hospital("Hospitalxd", "whyisthatstillhere")
TEST_HOSPITAL.anadirPacientes(TEST_PACIENTE)
TEST_RUTINA = None


#Constantes que si se van a usar xd
PACIENTE_ELEGIDO = None
TERAPIA_ELEGIDA = None
OBJETIVO_ELEGIDO = None
RUTINA_ELEGIDA = None


def mostrar_ejercicios(marco, lista_ejercicios):
    MAX_COLUMNAS = 6
    columna_actual = 0
    fila_actual = 0

    variables_ejercicios = {}

    for ejercicio in lista_ejercicios:

        var = tk.StringVar()
        nombre_ejercicio = ejercicio.get_nombre()
        variables_ejercicios[nombre_ejercicio] = var

        boton_ejercicio = ttk.Radiobutton(
            marco,
            text= nombre_ejercicio.replace("_", " ").title(),
            value= ejercicio.get_nombre(),
            variable=var,
            onvalue = True,
            offvalue = False
        )

        boton_ejercicio.grid(row=fila_actual, column=columna_actual, sticky=tk.W)

        columna_actual += 1
        if columna_actual >= MAX_COLUMNAS:
            columna_actual = 0
            fila_actual += 1

    return variables_ejercicios

def obtener_ejercicios_seleccionados(dict_var_ejercicios):
    ejercicios = []
    for nombre, var in dict_var_ejercicios.items():
        if var.get():
            ejercicios.append(nombre)

def mostrar_ejercicios_posibles(marco):
    ejercicios_para_mostrar = RUTINA_ELEGIDA.getEjerciciosPosibles()
    mostrar_ejercicios(marco, ejercicios_para_mostrar)

def mostrar_ejercicios_ordenados(marco):
    ejercicios_para_mostrar = RUTINA_ELEGIDA.getEjerciciosOrdenados()
    mostrar_ejercicios(marco, ejercicios_para_mostrar)

def convertir_ejercicios(entrada):
    nombres_ejercicios = entrada.split(" ")
    ejercicios_convertidos = []
    try:
        for nombre in nombres_ejercicios:
            ejercicio = Ejercicio[nombre]  # Asumiendo Ejercicio es un Enum
            ejercicios_convertidos.append(ejercicio)
    except KeyError:
        indicar_entrada_invalida()
    return ejercicios_convertidos


def screen_rutina(paciente):
    print(BLUE + "Bienvenido al generador de rutinas :D" + RESET)
    una_rutina = generar_rutina(paciente)
    generar_ejercicios_ordenados(una_rutina)
    agregar_ejercicios_adicionales(una_rutina)
    eliminar_ejercicios(una_rutina)
    paciente.get_historia_clinica().actualizar_historial_rutinas(una_rutina)
    print(BLUE + "La rutina ha sido guardada en la historia clínica" + RESET)
    print(BLUE + "Gracias por usar nuestro generador :D" + RESET)

# Funciones GUI
def obtener_paciente():
    global PACIENTE_ELEGIDO
    try:
        paciente_a_buscar = variable_paciente.get() 
        PACIENTE_ELEGIDO = TEST_HOSPITAL.buscarPaciente(paciente_a_buscar)

    except tk.TclError:
        messagebox.showerror("Error", "Por favor ingrese los números del documento de identificación, sin espacios ni símbolos.")
        return
    
    if not PACIENTE_ELEGIDO:
        messagebox.showerror("404 Paciente not found", "Paciente no encontrado, por favor verifique los datos ingresados.")
        return

def seleccionar_tipo_terapia(opcion):
    titulo_menu.set(opcion)
    global TERAPIA_ELEGIDA
    TERAPIA_ELEGIDA = TipoTerapia[opcion.upper()]

def seleccionar_tipo_objetivo():
    objetivo = variable_objetivo.get()
    global OBJETIVO_ELEGIDO
    OBJETIVO_ELEGIDO = TipoObjetivo[objetivo]

def crear_rutina():
    global RUTINA_ELEGIDA
    try:
        RUTINA_ELEGIDA = Rutina(PACIENTE_ELEGIDO, TERAPIA_ELEGIDA, OBJETIVO_ELEGIDO)
    except (TypeError, AttributeError) as e:
        messagebox.showerror("Datos incompletos", "Por favor llene todos los campos correctamente antes de presionar en siguiente.")
    print(RUTINA_ELEGIDA.getEjerciciosPosibles())
    mostrar_ejercicios_posibles(marco_ejercicios_posibles)


# GUI
FUENTE_REGULAR = "Montserrat 10"
FUENTE_TITULO = "Montserrat 24 bold"
FUENTE_SUBTITULO = "Montserrat 12"

MARGEN_ESTANDAR = 10

root = tk.Tk()
root.geometry("900x600")
root.title("Funcionalidad 4 AHAHA")

# Estilos para botones 
style = ttk.Style()

style.layout("FUENTE_REGULAR_MENUBTN", style.layout("TMenubutton"))
style.configure("FUENTE_REGULAR_MENUBTN", font=FUENTE_REGULAR)

style.layout("FUENTE_REGULAR_ROUNDBTN", style.layout("Custom.TRadiobutton"))
style.configure("FUENTE_REGULAR_ROUNDBTN", font=FUENTE_REGULAR)

style.layout("FUENTE_REGULAR_BTN", style.layout("Custom.TButton"))
style.configure("FUENTE_REGULAR_BTN", font=FUENTE_REGULAR)


# Seccion donde esta todo
marco_principal = ttk.Frame(root)
marco_principal.pack(expand=True, fill="both")

titulo_principal = ttk.Label(marco_principal, text="Generador de Rutinas", font=FUENTE_TITULO)
titulo_principal.pack(pady=(25, 20))

#Seccion paciente
marco_pregunta_paciente = ttk.Frame(marco_principal)
variable_paciente = tk.IntVar(value="")
pregunta_paciente = ttk.Label(
    marco_pregunta_paciente, 
    text="Ingrese el número de identificacion del paciente.",
    font=FUENTE_REGULAR
    )
entrada_paciente = ttk.Entry(
    marco_pregunta_paciente, 
    textvariable= variable_paciente,
    font=FUENTE_REGULAR,
    )
boton_paciente = ttk.Button(
    marco_pregunta_paciente,
    text="Ingresar Paciente",
    style="FUENTE_REGULAR_BTN",
    command=obtener_paciente
)
pregunta_paciente.pack()
entrada_paciente.pack(side="left", pady=MARGEN_ESTANDAR)
boton_paciente.pack(side="left", pady=MARGEN_ESTANDAR)
marco_pregunta_paciente.pack(pady=(0, MARGEN_ESTANDAR))

#Seccion tipo terapia
marco_pregunta_terapia = ttk.Frame(marco_principal)
titulo_menu = tk.StringVar()
titulo_menu.set("Selecciona el tipo de terapia")
menu_pregunta_terapia = ttk.Menubutton(marco_pregunta_terapia, textvariable=titulo_menu, style="FUENTE_REGULAR_MENUBTN")
submenu_pregunta_terapia = tk.Menu(menu_pregunta_terapia, tearoff=False)
submenu_pregunta_terapia.add_command(
    label="Acondicionamiento", 
    command=lambda: seleccionar_tipo_terapia("Acondicionamiento"), 
    font=FUENTE_REGULAR
    )
submenu_pregunta_terapia.add_command(
    label="Rehabilitacion", 
    command=lambda: seleccionar_tipo_terapia("Rehabilitacion"), 
    font=FUENTE_REGULAR
    )
menu_pregunta_terapia["menu"] = submenu_pregunta_terapia
menu_pregunta_terapia.pack()
marco_pregunta_terapia.pack(pady=(0,20))

# Seccion tipo objetivo
marco_pregunta_objetivo = ttk.Frame(marco_principal, borderwidth=10, relief="solid")
pregunta_objetivo = ttk.Label(
    marco_pregunta_objetivo, 
    text = "Indique el objetivo de la terapia.",
    font=FUENTE_REGULAR
    )
variable_objetivo = tk.StringVar()
boton_fortalecimiento_muscular = ttk.Radiobutton(
    marco_pregunta_objetivo, 
    text="Fortalecimiendo muscular",
    value= "FORTALECIMIENTO_MUSCULAR",
    variable=variable_objetivo,
    style="FUENTE_REGULAR_ROUNDBTN",
    command = seleccionar_tipo_objetivo
    )
boton_incremento_elasticidad = ttk.Radiobutton(
    marco_pregunta_objetivo, 
    text="Incremento de elasticidad",
    value= "INCREMENTO_ELASTICIDAD",
    variable=variable_objetivo,
    style="FUENTE_REGULAR_ROUNDBTN",
    command = seleccionar_tipo_objetivo
    )
boton_incremento_velocidad = ttk.Radiobutton(
    marco_pregunta_objetivo,
    text="Incremento de velocidad",
    value= "INCREMENTO_VELOCIDAD",
    variable=variable_objetivo,
    style="FUENTE_REGULAR_ROUNDBTN",
    command = seleccionar_tipo_objetivo
    )
boton_mejora_equilibrio = ttk.Radiobutton(
    marco_pregunta_objetivo, 
    text="Mejora del equilibrio",
    value= "MEJORA_DEL_EQUILIBRIO",
    variable=variable_objetivo,
    style="FUENTE_REGULAR_ROUNDBTN",
    command = seleccionar_tipo_objetivo
    )
boton_recuperacion_osea = ttk.Radiobutton(
    marco_pregunta_objetivo, 
    text="Recuperación de lesion osea",
    value= "RECUPERACION_LESION_OSEA",
    variable=variable_objetivo,
    style="FUENTE_REGULAR_ROUNDBTN",
    command = seleccionar_tipo_objetivo
    )
boton_recuperacion_muscular = ttk.Radiobutton(
    marco_pregunta_objetivo, 
    text="Recuperacion de lesion muscular",
    value= "RECUPERACION_LESION_MUSCULAR",
    variable=variable_objetivo,
    style="FUENTE_REGULAR_ROUNDBTN",
    command = seleccionar_tipo_objetivo
    )

BTN_PAD_VERTICAL = MARGEN_ESTANDAR
pregunta_objetivo.grid(pady=(0, MARGEN_ESTANDAR), row=0, column=0, columnspan=3)
boton_fortalecimiento_muscular.grid(row=1, column=0, padx=BTN_PAD_VERTICAL)
boton_incremento_elasticidad.grid(row=1, column=1, padx=BTN_PAD_VERTICAL)
boton_incremento_velocidad.grid(row=1, column=2, padx=BTN_PAD_VERTICAL)
boton_mejora_equilibrio.grid(row=2, column=0, padx=BTN_PAD_VERTICAL)
boton_recuperacion_osea.grid(row=2, column=1, padx=BTN_PAD_VERTICAL)
boton_recuperacion_muscular.grid(row=2, column=2, padx=BTN_PAD_VERTICAL)
marco_pregunta_objetivo.pack()


# Boton enviar
boton_enviar = ttk.Button(
    marco_principal,
    text="Siguiente",
    style="FUENTE_REGULAR_BTN",
    command= crear_rutina
    )
boton_enviar.pack(pady= (MARGEN_ESTANDAR,0))

# Seccion ejercicios para elegir
marco_ejercicios_posibles = ttk.Frame(marco_principal, borderwidth=10, relief="solid")
titulo_ejercicios = ttk.Label(marco_ejercicios_posibles, text="Ejercicios", font=FUENTE_SUBTITULO)

titulo_ejercicios.pack()
marco_ejercicios_posibles.pack(pady=(MARGEN_ESTANDAR, MARGEN_ESTANDAR))



root.mainloop()