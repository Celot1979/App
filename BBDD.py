import sqlite3
from tkinter import messagebox
from tools import *

def conexionBBDD():
    miConexion = sqlite3.connect("Datos.db")
    miCursor= miConexion.cursor()
    try:
        miCursor.execute("""CREATE TABLE formulario(ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) NOT NULL, 
        APELLIDOS VARCHAR(50) NOT NULL, 
        CONTRASEÑA VARCHAR(50) NOT NULL, 
        DIRECCION VARCHAR(50) NOT NULL, 
        COMENTARIO VARCHAR(100)NOT NULL)""")
        messagebox.showinfo("CONEXION", "Base de Datos Creada Exitosomanete")
    except:
        messagebox.showinfo("CONEXION", "Conexión exitosa con la BBDD")

def eliminar_Tabla():
    miConexion = sqlite3.connect("Datos.db")
    miCursor= miConexion.cursor()
    miCursor.execute("DROP TABLE formulario")
    messagebox.showinfo("BORRADO EFECTUADO", "La tabla ha sido borrada con éxito")
    miConexion.close()

def eliminar_BBDD():
    miConexion = sqlite3.connect("Datos.db")
    miCursor= miConexion.cursor()
    miCursor.execute("DROP DATEBASE Datos.db")
    messagebox.showinfo("BORRADO EFECTUADO", "La tabla ha sido borrada con éxito")
    miConexion.close()
    


def crear(nombre,apellidos,contraseña,direccion,l6):
    miConexion = sqlite3.connect("Datos.db")
    miCursor= miConexion.cursor()
    try:
        datos_for= nombre.get(),apellidos.get(),contraseña.get(),direccion.get(),l6.get(1.0, "end-1c")
        miCursor.execute("INSERT INTO formulario VALUES(NULL,?,?,?,?,?)",(datos_for))
        
        miConexion.commit()
        miConexion.close()
    except:
        messagebox.showinfo("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión")
    limpiar_campos(nombre,apellidos,contraseña,direccion,l6)