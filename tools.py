from tkinter import *
from tkinter import messagebox

def salir(root):
    root.destroy()

def limpiar_campos(nombre,apellidos,contraseña,direccion,l6):
    nombre.set('')
    apellidos.set('')
    contraseña.set('')
    direccion.set('')
    l6.delete(1.0, "end-1c")
    

def lincencia():
    messagebox.showinfo("LICENCIA", "PROGRAMA CREADO CON PYTHON Y TKINTER(By Daniel Gil). Para cualquier duda visitar la documentación")

def acerca():
    messagebox.showinfo("INFORMACIÓN", "Contacto: zata_k@hotmail.com")
