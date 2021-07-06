from tkinter import *
from tkinter import messagebox
from tools import *
from BBDD import *


root = Tk()
root.geometry("300x300")
root.title("App")
lamina = Frame(root)
lamina.pack(expand=1)
l6= Text(lamina,width = 25,height =10)
l6.grid(row=6,column=2)
miscroll=Scrollbar(lamina, command= l6.yview)
miscroll.grid(row=6,column=3,stick="nsew")
l6.config(yscrollcommand=miscroll.set)



informacion_comentario = l6.get("1.0",'end-1c')
print(informacion_comentario)

b1= Button(lamina,text="Create")
b1.grid(row=7,column=1)
root.mainloop()