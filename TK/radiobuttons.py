from tkinter import *


def start():

    def seleccionar():
        monitor.config(text=opcion.get())

    def reset():
        opcion.set(None)
        monitor.config(text="")

    # Configuración de la raiz
    root = Tk()

    opcion = IntVar()

    Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=seleccionar).pack()
    Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=seleccionar).pack()
    Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=seleccionar).pack()

    monitor = Label(root)
    monitor.pack()

    Button(root, text="Reiniciar", command=reset).pack()

    #  Finalmente bucle de la aplicación
    root.mainloop()


if __name__ == '__main__':
    start()
