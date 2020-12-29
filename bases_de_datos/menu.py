import sqlite3
from tkinter import *

# Configuración de la raiz
root = Tk()
root.title("El Mar - Menú")
root.resizable(0, 0)
root.config(bd=25, relief="sunken")

Label(root, text="   El Mar   ", fg="darkgreen", font=("Times New Roman", 28, "bold italic")).pack()
Label(root, text="Menú del Día", fg="green", font=("Times New Roman", 24, "bold italic")).pack()

# Separación de títulos y categorías
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# Buscar las categorías y platos de la bd
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    Label(root, text=categoria[1], fg="black", font=("Times New Roman", 20, "bold italic")).pack()
    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id = {}".format(categoria[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1], fg="grey", font=("Times New Roman", 15, "bold italic")).pack()

conexion.close()

# Precio del Menú
Label(root, text="S/. 12.0", fg="darkgreen", font=("Times New Roman", 15, "bold italic")).pack(side="right")

# Finalmente ejecutamos el bucle
root.mainloop()
