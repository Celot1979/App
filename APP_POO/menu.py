from tkinter import Tk, messagebox
import tkinter as tk

class men:
    def __init__(self,ventana):
        #Crear barra de menú
        self.ventana= ventana
        self.menubar = tk.Menu(self.ventana)
        #Creación de submenus
        self.BBDDmenu = tk.Menu(self.menubar,tearoff=0)
        self.Borrarmenu = tk.Menu(self.menubar,tearoff=0)
        self.CRUDmenu = tk.Menu(self.menubar,tearoff=0)
        self.helpmenu = tk.Menu(self.menubar,tearoff=0)   
        #Añadimos los submenus antes creados a la barra del menú
        self.menubar.add_cascade(label="BBFF", menu = self.BBDDmenu)
        self.menubar.add_cascade(label="Borrar", menu = self.Borrarmenu)
        self.menubar.add_cascade(label="CRUD", menu = self.CRUDmenu)
        self.menubar.add_cascade(label="Ayuda", menu = self.helpmenu)

        #Añadimos los comandos de cada submenú
        self.BBDDmenu.add_command(label="CREAR BBDD")
        self.BBDDmenu.add_command(label="Borrar Tabla de BBDD ")
        self.BBDDmenu.add_command(label="SALIR")


        self.CRUDmenu.add_command(label="CREATE")
        self.CRUDmenu.add_command(label="READ")
        self.CRUDmenu.add_command(label="UPDATE")
        self.CRUDmenu.add_command(label="DELATE")


        self.Borrarmenu.add_command(label="Borrar campos de texto")


        self.helpmenu.add_command(label="AYUDA DE")
        self.helpmenu.add_command(label="LINCENCIA")