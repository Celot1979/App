from tkinter import Tk, messagebox
import tkinter as tk

class men:
    def __init__(self,ventana):
        self.ventana = ventana
        self.menu = tk.Frame(self.ventana)
        self.menu.pack()
        self.menubar = tk.Menu(self.menu)
        self.ventana.config(menu=self.menubar, width = 300, height = 300)

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