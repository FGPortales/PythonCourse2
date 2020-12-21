from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog


def start():

    # Configuración de la raiz
    root = Tk()

    def test():
        # MessageBox.showinfo("Hola!", "Hola Mundo")
        # MessageBox.showwarning("Alerta", "Sesión para administradores.")
        # MessageBox.showerror("Error!", "Ha ocurrido un error inesperado!")
        # resultado = MessageBox.askquestion("Salir", "Está seguro que desea slair sin guardar?")
        # if resultado == 'yes':
        #     root.destroy()
        # resultado = MessageBox.askokcancel("Salir", "Sobreescribir el fichero actual?")
        # resultado = MessageBox.askyesno("Salir", "Está seguro que desea slair sin guardar?")  # Con booleano
        # if resultado:
        #     root.destroy()
        # resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
        # if resultado:
        #     root.destroy()
        # color = ColorChooser.askcolor(title="Eligue un color")
        # print(color)
        # ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:/",
        #                                   filetypes=(("Fichero de Texto", "*.txt"),
        #                                              ("Fichero de Texto avanzado", "*.txt2"),
        #                                              ("Todos los ficheros", "*.*")))
        # print(ruta)
        #  Equivale a open('ruta', 'w')
        fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="r+", defaultextension=".txt")
        print(fichero)
    Button(root, text="Clícame", command=test).pack()

    #  Finalmente bucle de la aplicación
    root.mainloop()


if __name__ == '__main__':
    start()
