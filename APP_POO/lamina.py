from tkinter import Tk, messagebox
import tkinter as tk

class lamina:
    def __init__(self,ventana):
        self.ventanaF = ventana
        self.Lamina = tk.Frame(self.ventanaF)
        self.Lamina.pack(expand=1)
        #Creacion de Interfaz en Frame en
        #StringVar
        self. nombre= tk.StringVar()
        self. apellido= tk.StringVar()
        self. contraseña= tk.StringVar()
        self. direccion= tk.StringVar()
        self.et1 =tk.Label(self.Lamina, text="NOMBRE")
        self.et1.grid(row=1,column=1)

        self.et2 =tk.Label(self.Lamina, text="APELLIDOS")
        self.et2.grid(row=2,column=1)

        self.et3 =tk.Label(self.Lamina, text="CONTRASEÑA")
        self.et3.grid(row=3,column=1)

        self.et4 =tk.Label(self.Lamina, text="DIRECCION")
        self.et4.grid(row=4,column=1)

        self.et5 =tk.Label(self.Lamina, text="COMENTARIOS")
        self.et5.grid(row=5,column=1)


        self.en1 =tk.Entry(self.Lamina, textvariable= self.nombre)
        self.en1.grid(row=1,column=2)

        self.en2 =tk.Entry(self.Lamina, textvariable= self.apellido)
        self.en2.grid(row=2,column=2)

        self.en3 =tk.Entry(self.Lamina, textvariable= self.contraseña)
        self.en3.grid(row=3,column=2)

        self.en4 =tk.Entry(self.Lamina, textvariable= self.direccion)
        self.en4.grid(row=4,column=2)

        self.b1 = tk.Button(self.Lamina, text="CREATE")
        self.b1.grid(row=6,column=1)
        self.b2 = tk.Button(self.Lamina, text="READ")
        self.b2.grid(row=6,column=2)
        self.b3 = tk.Button(self.Lamina, text="UPDATE")
        self.b3.grid(row=6,column=3)
        self.b4 = tk.Button(self.Lamina, text="DELATE")
        self.b4.grid(row=6,column=4)