from tkinter import *

# Configuración de la raiz
root = Tk()

label = Label(root, text="Nombre muy largo")
label.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, sticky="e") #  sticky ubicar entry (e -> este/ w -> west /sur / norte)
entry.config(justify="right", state="normal")

label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, sticky="e")
entry2.config(justify="center", show="?")




#  Finalmente bucle de la aplicación
root.mainloop()