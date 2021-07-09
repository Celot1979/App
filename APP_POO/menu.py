from tkinter import Tk, messagebox
import tkinter as tk
from BBDD import *
from tools import *


class men:
    def __init__(self,ventana):
        self.ventana = ventana
        self.menu = tk.Frame(self.ventana)
        self.menu.pack()
        self.menubar = tk.Menu(self.menu)
        

        #Creación de submenus
        self.BBDDmenu = tk.Menu(self.menubar,tearoff=0)
        self.Borrarmenu = tk.Menu(self.menubar,tearoff=0)
        self.CRUDmenu = tk.Menu(self.menubar,tearoff=0)
        self.helpmenu = tk.Menu(self.menubar,tearoff=0)
        #Funciones 
        def salir(self):
            self.ventana.destroy()
        #Añadimos los submenus antes creados a la barra del menú
        self.menubar.add_cascade(label="BBFF", menu = self.BBDDmenu)
        self.menubar.add_cascade(label="Borrar", menu = self.Borrarmenu)
        self.menubar.add_cascade(label="CRUD", menu = self.CRUDmenu)
        self.menubar.add_cascade(label="Ayuda", menu = self.helpmenu)
        #Añadimos los comandos de cada submenú
        self.BBDDmenu.add_command(label="CREAR BBDD", command =conexionBBDD)
        self.BBDDmenu.add_command(label="Borrar Tabla de BBDD ",command =eliminar_Tabla)
        self.BBDDmenu.add_command(label="SALIR",command=lambda: salir(self))


        self.CRUDmenu.add_command(label="CREATE",command=lambda:crear(self.nombre,self.apellido,self.contraseña,self.direccion,self.l6))
        self.CRUDmenu.add_command(label="READ",command=lambda:leer(self.id,self.nombre,self.apellido,self.contraseña,self.direccion,self.l6))
        self.CRUDmenu.add_command(label="UPDATE",command=lambda:actualizar(self.id,self.nombre,self.apellido,self.contraseña,self.direccion,self.l6))
        self.CRUDmenu.add_command(label="DELATE",command=lambda:borrar(self.id,self.nombre,self.apellido,self.contraseña,self.direccion,self.l6))


        self.Borrarmenu.add_command(label="Borrar campos de texto")


        self.helpmenu.add_command(label="AYUDA DE",command= acerca)
        self.helpmenu.add_command(label="LINCENCIA",command= lincencia)

        self.ventana.config(menu=self.menubar, width = 300, height = 300)