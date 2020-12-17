from tkinter import *

root = Tk()
root.title("Hola Freddy")
root.resizable(1, 1)
root.iconbitmap('hongo.ico')

frame = Frame(root, width=480, height=320)
# frame.pack(fill="y", expand=1)
frame.pack(fill="both", expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")


root.config(cursor="arrow")
root.config(bg="blue")  # background
root.config(bd=15)  # border
root.config(relief="ridge")

# Abajo del _todo
root.mainloop()