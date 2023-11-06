# Creación ventana principal
from tkinter import *

class ventana_inicio(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # CONFIGURACION PARAMETROS PRINCIPALES DE LA VENTANA
        self.geometry("800x500")
        self.title("Inicio")
        self.option_add("*tearOff", False)
        self.resizable(0,0) # Para que no se pueda expandir la venta
        # CONFIGURACION VR--TEXTO HDV DESARROLLADORES

       
if __name__ == "__main__":
    ventana_inicios = ventana_inicio()
    ventana_inicios.mainloop()