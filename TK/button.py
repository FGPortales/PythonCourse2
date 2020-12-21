from tkinter import *

CONT = 0


def start():

    def sumar():
        r.set(float(n1.get()) + float(n2.get()))
        borrar()

    def borrar():
        n1.set("")
        n2.set("")


    # Configuración de la raiz
    root = Tk()
    root.config(bd=15)

    n1 = StringVar()
    n2 = StringVar()
    r = StringVar()

    Label(root, text="Número 1").pack()
    Entry(root, justify="center", textvariable=n1).pack() #  Primer número
    Label(root, text="Número 2").pack()
    Entry(root, justify="center", textvariable=n2).pack() #  Segundo número
    Label(root, text=" ").pack()
    Button(root, text="Sumar", command=sumar).pack()
    Label(root, text="\nResultado").pack()
    Entry(root, justify="center", textvariable=r, state="disabled").pack() #  Tercer número

    #  Finalmente bucle de la aplicación
    root.mainloop()


if __name__ == '__main__':
    start()