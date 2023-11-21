""" Maria Paula Ardila, Daniela Cristina Garcia Torres, Leopold Pierre Lanard
Jose Nicolas Duque Linares, Ronal Yesid Castro Romero """
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from src.ui_main.ventana_principal import ventana_principal

imagen_seleccionada = 0
desarrollador = 0


def ventana_inicial(hospital):
    def desarrollador4():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Maria Paula Ardila Otero",
                      font=("Comic Sans MS", 20))
        email.config(text="mardilao@unal.edu.co", font=("Comic Sans MS", 12))
        github.config(text="github.com/mariasaurius",
                      font=("Comic Sans MS", 12))
        carrera.config(text="Ciencias de la Computacion",
                       font=("Comic Sans MS", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize(
            (foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize(
            (foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize(
            (foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize(
            (foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def desarrollador3():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Ronal Yesid Castro Romero",
                      font=("Comic Sans MS", 20))
        email.config(text="rocastror@unal.edu.co", font=("Comic Sans MS", 12))
        github.config(text="github.com/ronalcastro97",
                      font=("Comic Sans MS", 12))
        carrera.config(text="Ciencias de la computación",
                       font=("Comic Sans MS", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize(
            (foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize(
            (foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize(
            (foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize(
            (foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def desarrollador2():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Leopold Pierre Lanard",
                      font=("Comic Sans MS", 20))
        email.config(text="llanard@unal.edu.co", font=("Comic Sans MS", 12))
        github.config(text="github.com/bosettii", font=("Comic Sans MS", 12))
        carrera.config(text="Ciencias de la computación",
                       font=("Comic Sans MS", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize(
            (foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize(
            (foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize(
            (foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize(
            (foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def desarrollador1():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Jose Nicolas Duque Linares",
                      font=("Comic Sans MS", 20))
        email.config(text="joduquela@unal.edu.co", font=("Comic Sans MS", 12))
        github.config(text="github.com/NICOXO", font=("Comic Sans MS", 12))
        carrera.config(text="Ingenieria de Sistemas e Informática",
                       font=("Comic Sans MS", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize(
            (foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize(
            (foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize(
            (foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize(
            (foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def desarrollador0():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Daniela Cristina Garcia Torres",
                      font=("Comic Sans MS", 20))
        email.config(text="dagarciat@unal.edu.co", font=("Comic Sans MS", 12))
        github.config(text="github.com/daninjaa", font=("Comic Sans MS", 12))
        carrera.config(text="Ciencias de la computación",
                       font=("Comic Sans MS", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize(
            (foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize(
            (foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize(
            (foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize(
            (foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def cambiar_hoja_de_vida(event):
        global desarrollador

        desarrollador = (desarrollador + 1) % 5

        if desarrollador == 0:
            desarrollador0()
        elif desarrollador == 1:
            desarrollador1()
        elif desarrollador == 2:
            desarrollador2()
        elif desarrollador == 3:
            desarrollador3()
        elif desarrollador == 4:
            desarrollador4()

    def cambiar_imagen_aplicacion(event):
        global tk_cambio_aplicacion
        global imagen_seleccionada

        width = canvas_imagenes_aplicacion.winfo_width()
        height = canvas_imagenes_aplicacion.winfo_height()

        imagen_seleccionada = (imagen_seleccionada + 1) % len(lista_imagenes)

        imagen_aplicacion_nueva = lista_imagenes[imagen_seleccionada]

        tk_cambio_aplicacion = ImageTk.PhotoImage(
            imagen_aplicacion_nueva.resize((width, height)))

        canvas_imagenes_aplicacion.create_image(
            0, 0, image=tk_cambio_aplicacion, anchor="nw")

    def acomodar_foto4(event):
        global tk_foto4

        width = event.width
        height = event.height

        foto4 = lista_fotos[desarrollador][3]
        tk_foto4 = ImageTk.PhotoImage(foto4.resize((width, height)))

        foto11.create_image(0, 0, image=tk_foto4, anchor="nw")

    def acomodar_foto3(event):
        global tk_foto3

        width = event.width
        height = event.height

        foto3 = lista_fotos[desarrollador][2]
        tk_foto3 = ImageTk.PhotoImage(foto3.resize((width, height)))

        foto10.create_image(0, 0, image=tk_foto3, anchor="nw")

    def acomodar_foto2(event):
        global tk_foto2

        width = event.width
        height = event.height

        foto2 = lista_fotos[desarrollador][1]
        tk_foto2 = ImageTk.PhotoImage(foto2.resize((width, height)))

        foto01.create_image(0, 0, image=tk_foto2, anchor="nw")

    def acomodar_foto1(event):
        global tk_foto1

        width = event.width
        height = event.height

        foto1 = lista_fotos[desarrollador][0]
        tk_foto1 = ImageTk.PhotoImage(foto1.resize((width, height)))

        foto00.create_image(0, 0, image=tk_foto1, anchor="nw")

    def acomodar_imagen_aplicacion(event):
        global tk_aplicacion

        width = event.width
        height = event.height

        imagen_aplicacion_nueva = lista_imagenes[imagen_seleccionada].resize(
            (width, height))
        tk_aplicacion = ImageTk.PhotoImage(imagen_aplicacion_nueva)

        canvas_imagenes_aplicacion.create_image(
            0, 0, image=tk_aplicacion, anchor="nw")

    def descripcion():
        descripcion_texto = "Athena OlympiCare, centro de medicina deportiva con ortopedistas, fisioterapeutas y nutricionistas, ofrece consultas, cirugías y terapias para todos los niveles deportivos."
        messagebox.showinfo("Descripcion", descripcion_texto)

    ventana = tk.Tk()
    ventana.title("Athena OlympiCare - Centro de medicina deportiva")
    # Cambiar el ícono de la ventana
    ventana.iconbitmap("src/ui_main/imagenes/icono.ico")  
    ventana.geometry("1280x720")
    ventana.protocol("WM_DELETE_WINDOW", hospital.serializar())

    # Crear un objeto de estilo
    style = ttk.Style()

    # Definir estilo personalizado
    style.configure("Red.TFrame", background="orchid1")

    # Definir un estilo personalizado para Label
    style.configure("Custom.TLabel", background="pale turquoise",
                    foreground="goldenrod4")
    style.configure("Custom1.TLabel", background="PaleGreen1",
                    foreground="purple")

    # Menu inicio
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)
    opcion_archivo = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=opcion_archivo)
    opcion_archivo.add_command(label="Descripcion", command=descripcion)
    opcion_archivo.add_command(label="Salir", command=lambda: [
                               hospital.serializar(), ventana.destroy()])

    # Frames principales
    frame_p1 = ttk.Frame(ventana)
    frame_p2 = ttk.Frame(ventana)

    # Mensaje de bienvenida
    frame_p3 = ttk.Frame(frame_p1, style="Red.TFrame")
    bienvenida = ttk.Label(frame_p3, text="Bienvenido a Athena OlympiCare",
                           style="Custom.TLabel", anchor="center", font=("Gabriola", 30, "bold"))

    # Imagenes de la aplicacion
    frame_p4 = ttk.Frame(frame_p1)
    p4_imagenes = ttk.Frame(frame_p4)
    p4_imagenes.configure(borderwidth=7, relief="solid", padding=0)
    canvas_imagenes_aplicacion = tk.Canvas(p4_imagenes)
    lista_imagenes = [Image.open("src/ui_main/imagenes/aplicacion/imagen1.jpg").resize((1000, 1000)),
                      Image.open(
                          "src/ui_main/imagenes/aplicacion/imagen2.jpg").resize((1000, 1000)),
                      Image.open(
                          "src/ui_main/imagenes/aplicacion/imagen3.jpg").resize((1000, 1000)),
                      Image.open(
                          "src/ui_main/imagenes/aplicacion/imagen4.jpg").resize((1000, 1000)),
                      Image.open("src/ui_main/imagenes/aplicacion/imagen5.jpg").resize((1000, 1000))]

    # Boton para continuar
    p4_continuar = ttk.Frame(frame_p4)
    style = ttk.Style()
    style.configure("My.TButton.TButton", foreground="black",
                    background="PaleGreen1", font=("Ink Free", 15, "bold"))

    continuar = ttk.Button(p4_continuar, text="Ingresar a la aplicación", style="My.TButton.TButton",
                           command=lambda: [ventana.destroy(), ventana_principal(hospital)])

    # Hoja de vida desarrolladores
    frame_p5 = ttk.Frame(frame_p2)
    nombre = ttk.Label(frame_p5, style="Custom1.TLabel", anchor="center")
    email = ttk.Label(frame_p5, style="Custom1.TLabel", anchor="center")
    github = ttk.Label(frame_p5, style="Custom1.TLabel", anchor="center")
    carrera = ttk.Label(frame_p5, style="Custom1.TLabel", anchor="center")
# ---------------------------------------------------------------------------------
    nombre.config(text="Daniela Cristina Garcia Torres",
                  font=("Comic Sans MS", 20))
    email.config(text="dagarciat@unal.edu.co", font=("Comic Sans MS", 12))
    github.config(text="github.com/daninjaa", font=("Comic Sans MS", 12))
    carrera.config(text="Ciencias de la computación",
                   font=("Comic Sans MS", 12))

    # Fotos desarrolladores
    frame_p6 = ttk.Frame(frame_p2)
    lista_fotos = [[Image.open("src/ui_main/imagenes/desarrolladores/Daniela/foto1.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Daniela/foto2.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Daniela/foto3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/desarrolladores/Daniela/foto4.jpg").resize((1000, 1000))],

                   [Image.open("src/ui_main/imagenes/desarrolladores/Jose/foto1.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Jose/foto2.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Jose/foto3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/desarrolladores/Jose/foto4.jpg").resize((1000, 1000))],

                   [Image.open("src/ui_main/imagenes/desarrolladores/Leo/foto1.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Leo/foto2.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Leo/foto3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/desarrolladores/Leo/foto4.jpg").resize((1000, 1000))],

                   [Image.open("src/ui_main/imagenes/desarrolladores/Ronal/foto1.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Ronal/foto2.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Ronal/foto3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/desarrolladores/Ronal/foto4.jpg").resize((1000, 1000))],

                   [Image.open("src/ui_main/imagenes/desarrolladores/Maria/foto1.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Maria/foto2.jpg").resize((1000, 1000)),
                    Image.open(
                        "src/ui_main/imagenes/desarrolladores/Maria/foto3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/desarrolladores/Maria/foto4.jpg").resize((1000, 1000))],
                   ]

    foto00 = tk.Canvas(frame_p6)
    foto01 = tk.Canvas(frame_p6)
    foto10 = tk.Canvas(frame_p6)
    foto11 = tk.Canvas(frame_p6)

    # Diseño
    frame_p1.pack(side="left", expand=True, fill="both")
    frame_p2.pack(side="left", expand=True, fill="both")

    frame_p3.pack(fill="both")
    bienvenida.pack(expand=True, fill="both", ipady=10, padx=10, pady=10)

    frame_p4.pack(expand=True, fill="both")
    p4_imagenes.pack(expand=True, fill="both")
    canvas_imagenes_aplicacion.pack(expand=True, fill="both")
    canvas_imagenes_aplicacion.bind("<Configure>", acomodar_imagen_aplicacion)
    canvas_imagenes_aplicacion.bind("<Enter>", cambiar_imagen_aplicacion)

    p4_continuar.pack(fill="both")
    continuar.pack(expand=True, fill="both", ipady=10, padx=10, pady=10)

    frame_p5.pack(fill="both")
    nombre.pack(expand=True, fill="both", ipady=5)
    email.pack(expand=True, fill="both")
    github.pack(expand=True, fill="both")
    carrera.pack(expand=True, fill="both")
    nombre.bind("<Button-1>", cambiar_hoja_de_vida)
    email.bind("<Button-1>", cambiar_hoja_de_vida)
    github.bind("<Button-1>", cambiar_hoja_de_vida)
    carrera.bind("<Button-1>", cambiar_hoja_de_vida)

    frame_p6.pack(expand=True, fill="both")
    frame_p6.columnconfigure(0, weight=1, uniform="fotos")
    frame_p6.columnconfigure(1, weight=1, uniform="fotos")
    frame_p6.rowconfigure(0, weight=1)
    frame_p6.rowconfigure(1, weight=1)
    foto00.grid(row=0, column=0, sticky="nsew")
    foto01.grid(row=0, column=1, sticky="nsew")
    foto10.grid(row=1, column=0, sticky="nsew")
    foto11.grid(row=1, column=1, sticky="nsew")
    foto00.bind("<Configure>", acomodar_foto1)
    foto01.bind("<Configure>", acomodar_foto2)
    foto10.bind("<Configure>", acomodar_foto3)
    foto11.bind("<Configure>", acomodar_foto4)

    ventana.mainloop()
