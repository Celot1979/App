from tkinter import Tk, messagebox
import tkinter as tk
from BBDD import *

class lamina:
    def __init__(self,ventana):
        self.ventanaF = ventana
        self.Lamina = tk.Frame(self.ventanaF)
        self.Lamina.pack(expand=1)
        #Creacion de Interfaz en Frame en
        #StringVar
        self.id = tk.StringVar()
        self.nombre= tk.StringVar()
        self.apellido= tk.StringVar()
        self.contraseña= tk.StringVar()
        self.direccion= tk.StringVar()
        self.et0 =tk.Label(self.Lamina, text="ID")
        self.et0.grid(row=1,column=1)

        

        self.et1 =tk.Label(self.Lamina, text="NOMBRE")
        self.et1.grid(row=2,column=1)

        self.et2 =tk.Label(self.Lamina, text="APELLIDOS")
        self.et2.grid(row=3,column=1)

        self.et3 =tk.Label(self.Lamina, text="CONTRASEÑA")
        self.et3.grid(row=4,column=1)

        self.et4 =tk.Label(self.Lamina, text="DIRECCION")
        self.et4.grid(row=5,column=1)

        self.et5 =tk.Label(self.Lamina, text="COMENTARIOS")
        self.et5.grid(row=6,column=1)

        self.en0 =tk.Entry(self.Lamina, textvariable= self.id)
        self.en0.grid(row=1,column=2) 

        self.en1 =tk.Entry(self.Lamina, textvariable= self.nombre)
        self.en1.grid(row=2,column=2)

        self.en2 =tk.Entry(self.Lamina, textvariable= self.apellido)
        self.en2.grid(row=3,column=2)

        self.en3 =tk.Entry(self.Lamina, textvariable= self.contraseña, show= "*")
        self.en3.grid(row=4,column=2)

        self.en4 =tk.Entry(self.Lamina, textvariable= self.direccion)
        self.en4.grid(row=5,column=2)

        self.l6= tk.Text(self.Lamina,width = 25,height =10)
        self.l6.grid(row=6,column=2)
        self.miscroll=tk.Scrollbar(self.Lamina, command= self.l6.yview)
        self.miscroll.grid(row=6,column=3,stick="nsew")
        self.l6.config(yscrollcommand=self.miscroll.set)



        self.b1 = tk.Button(self.Lamina, text="CREATE",command=lambda:crear(self.nombre,self.apellido,self.contraseña,self.direccion,self.l6))
        self.b1.grid(row=7,column=1)
        self.b2 = tk.Button(self.Lamina, text="READ",command=lambda:leer(self.id,self.nombre,self.apellido,self.contraseña,self.direccion,self.l6))
        self.b2.grid(row=7,column=2)
        self.b3 = tk.Button(self.Lamina, text="UPDATE",command=lambda:actualizar(self.id,self.nombre,self.apellido,self.contraseña,self.direccion,self.l6))
        self.b3.grid(row=7,column=3)
        self.b4 = tk.Button(self.Lamina, text="DELATE",command=lambda:borrar(self.id,self.nombre,self.apellido,self.contraseña,self.direccion,self.l6))
        self.b4.grid(row=7,column=4)

        self.menubar = tk.Menu(self.ventanaF)
        #Creación de submenus
        self.BBDDmenu = tk.Menu(self.menubar,tearoff=0)
        self.Borrarmenu = tk.Menu(self.menubar,tearoff=0)
        self.CRUDmenu = tk.Menu(self.menubar,tearoff=0)
        self.helpmenu = tk.Menu(self.menubar,tearoff=0)
        #Funciones 
        def salir(self):
            self.ventanaF.destroy()
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
       
        def borrar_campos(self):
            self.id.set('')
            self.nombre.set('')
            self.apellidos.set('')
            self.contraseña.set('')
            self.direccion.set('')
        

        self.Borrarmenu.add_command(label="Borrar campos de texto",command=borrar_campos)


        self.helpmenu.add_command(label="AYUDA DE",command= acerca)
        self.helpmenu.add_command(label="LINCENCIA",command= lincencia)

        self.ventanaF.config(menu=self.menubar, width = 300, height = 300)
            