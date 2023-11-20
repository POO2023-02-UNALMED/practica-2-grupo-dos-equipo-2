import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ventana_secundaria(tk.Toplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #Configuracion segunda ventana
        self.en_uso=False
        

if __name__ == "__main__":
    ventana_secundarias = ventana_secundaria
    ventana_secundaria.mainloop()
