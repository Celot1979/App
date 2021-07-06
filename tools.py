from tkinter import *
from tkinter import messagebox

def salir(root):
    root.destroy()

def limpiar_campos(nombre,apellidos,contraseña,direccion,comentarios):
    nombre.set('')
    apellidos.set('')
    contraseña.set('')
    direccion.set('')
    comentarios.set('')

def lincencia():
    messagebox.showinfo("LICENCIA", "PROGRAMA CREADO CON PYTHON Y TKINTER(By Daniel Gil). Para cualquier duda visitar la documentación")

def acerca():
    messagebox.showinfo("INFORMACIÓN", "Contacto: zata_k@hotmail.com")
