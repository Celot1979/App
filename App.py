from tkinter import *
from tkinter import messagebox
from tools import *
from BBDD import *


root = Tk()
root.geometry("300x500")
root.title("App")

#Frame
lamina = Frame(root)
lamina.pack(expand=1)

#Etiquetas
et1= Label(lamina,text="Id")
et1.grid(row=1, column=1)

et1= Label(lamina,text="Nombre")
et1.grid(row=2, column=1)

et2= Label(lamina,text="Apellidos")
et2.grid(row=3, column=1)



et3= Label(lamina,text="Contraseña")
et3.grid(row=4, column=1)

et4= Label(lamina,text="Domicilio")
et4.grid(row=5, column=1)

et6= Label(lamina,text="Comentarios")
et6.grid(row=6, column=1)




#Variables
id =StringVar()
nombre =StringVar()
apellidos =StringVar()
contraseña =StringVar()
direccion =StringVar()
#comentarios =StringVar()

#Caja de textos
l1= Entry(lamina, textvariable= id)
l1.grid(row=1,column=2)

l2= Entry(lamina, textvariable= nombre)
l2.grid(row=2,column=2)

l3= Entry(lamina, textvariable= apellidos)
l3.grid(row=3,column=2)

l4= Entry(lamina, textvariable= contraseña, show= "*")
l4.grid(row=4,column=2)

l5= Entry(lamina, textvariable= direccion)
l5.grid(row=5,column=2)

"""l6= Entry(lamina, textvariable= comentarios)
l6.grid(row=6,column=2,padx=10,pady=10,ipady=30)"""

l6= Text(lamina,width = 25,height =10)
l6.grid(row=6,column=2)
miscroll=Scrollbar(lamina, command= l6.yview)
miscroll.grid(row=6,column=3,stick="nsew")
l6.config(yscrollcommand=miscroll.set)
def info(l6):
    informacion_comentario = l6.get(1.0, "end-1c")
    print(informacion_comentario)


#Botones
b1= Button(lamina,text="Create",command= lambda: crear(nombre,apellidos,contraseña,direccion,l6))
b1.grid(row=7,column=1)

b2= Button(lamina,text="Read",command= lambda: leer(id,nombre,apellidos,contraseña,direccion,l6))
b2.grid(row=7,column=2)

b3= Button(lamina,text="Update",command= lambda: actualizar(id,nombre,apellidos,contraseña,direccion,l6))
b3.grid(row=7,column=3 , padx = 50 , pady = 30)

b4= Button(lamina,text="Delate",command= lambda: borrar(id,nombre,apellidos,contraseña,direccion,l6))
b4.grid(row=7,column=7,columnspan=2)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Menu
#Crear barra de menú
menubar = Menu(root)
#Creación de submenus
BBDDmenu = Menu(menubar,tearoff=0)
Borrarmenu = Menu(menubar,tearoff=0)
CRUDmenu = Menu(menubar,tearoff=0)
helpmenu = Menu(menubar,tearoff=0)
#Añadimos los submenus antes creados a la barra del menú
menubar.add_cascade(label="BBFF", menu = BBDDmenu)
menubar.add_cascade(label="Borrar", menu = Borrarmenu)
menubar.add_cascade(label="CRUD", menu = CRUDmenu)
menubar.add_cascade(label="Ayuda", menu = helpmenu)
#Funciones del menú 

#Añadimos los comandos de cada submenú
BBDDmenu.add_command(label="CREAR BBDD", command =conexionBBDD)
BBDDmenu.add_command(label="Borrar Tabla de BBDD ", command= eliminar_Tabla)
BBDDmenu.add_command(label="SALIR", command = lambda: salir(root))


CRUDmenu.add_command(label="CREATE",command= lambda: crear(nombre,apellidos,contraseña,direccion,l6))
CRUDmenu.add_command(label="READ",command= lambda: leer(nombre,apellidos,contraseña,direccion,l6))
CRUDmenu.add_command(label="UPDATE",command= lambda: actualizar(id,nombre,apellidos,contraseña,direccion,l6))
CRUDmenu.add_command(label="DELATE",command= lambda: borrar(id,nombre,apellidos,contraseña,direccion,l6))


Borrarmenu.add_command(label="Borrar campos de texto",command= lambda: limpiar_campos(nombre,apellidos,contraseña,direccion,comentarios))


helpmenu.add_command(label="AYUDA DE", command = acerca)
helpmenu.add_command(label="LINCENCIA", command = lincencia)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

root.config(menu=menubar)#Final del menú
root.mainloop()