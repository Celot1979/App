
from tkinter import Tk, messagebox
import tkinter as tk

from lamina import *


root = Tk()
class Ejemplo:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry("800x600")
        self.ventana.title("Ejemplo en POO")





if __name__ == "__main__":
    e=Ejemplo(root)   #Raiz
    f= lamina(root)   #Frame
    #m = men(root)     #Menu
    root.mainloop()