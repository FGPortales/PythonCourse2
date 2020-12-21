from tkinter import *


def start():

    def seleccionar():
        cadena=""
        if(leche.get()):
            cadena += "Con leche"
        else:
            cadena += "Sin leche"

        if(azucar.get()):
            cadena += " y con Azúcar"
        else:
            cadena += " y sin Azúcar"
        monitor.config(text=cadena)


    # Configuración de la raiz
    root = Tk()
    root.title("Cafeteria")
    root.config(bd=15)

    leche = IntVar()  # 1 si, 0 no
    azucar = IntVar()

    imagen = PhotoImage(file="imagen.gif")
    Label(root, image=imagen).pack(side="left")

    frame = Frame(root)
    frame.pack(side="right")

    Label(frame, text="¿Cómo quieres el café?").pack(anchor="w")
    Checkbutton(frame, text="Con Leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
    Checkbutton(frame, text="Con Azúcar", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

    monitor = Label(frame)
    monitor.pack()




    #  Finalmente bucle de la aplicación
    root.mainloop()


if __name__ == '__main__':
    start()
