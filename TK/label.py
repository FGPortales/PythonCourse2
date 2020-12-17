from tkinter import *

# Configuración de la raiz
root = Tk()
"""
# Variables dinámicas
texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="¡Hola Mundo!").pack(anchor="nw")
label = Label(root, text="¡Hola Mundo1!")
label.pack(anchor="center")
Label(root, text="¡Hola Mundo2!").pack(anchor="se")


label.config(bg="green", fg="yellow", font=("Verdana", 24))
label.config(textvariabl=texto)
"""

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")

#  Finalmente bucle de la aplicación
root.mainloop()