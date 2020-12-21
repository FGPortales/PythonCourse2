from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

PATH = ""  # store path of a file
TITLE = "EditorEX"


def start():

    def new_file():
        global PATH
        message.set("New File")
        PATH = ""
        text.delete(1.0, END)
        root.title(TITLE)

    def open_file():
        global PATH
        message.set("Open File")
        PATH = FileDialog.askopenfilename(
            initialdir='.',
            filetype=(("Text File", "*.txt"),),
            title="Open text file"
        )
        if PATH != "":
            file = open(PATH, 'r')
            content = file.read()
            text.delete(1.0, 'end')
            text.insert('insert', content)
            file.close()
            root.title(PATH + " -" + TITLE)

    def save_file():
        message.set("Save File")
        if PATH != "":
            content = text.get(1.0, 'end-1c')
            file = open(PATH, 'w+')
            file.write(content)
            file.close()
            message.set("File Saved Successfully")
        else:
            save_as_file()

    def save_as_file():
        global PATH
        message.set("Save File as")
        file = FileDialog.asksaveasfile(title="Save File", mode="w", defaultextension=".txt")
        if file is not None:
            PATH = file.name
            content = text.get(1.0, 'end-1c')
            file = open(PATH, 'w+')
            file.write(content)
            file.close()
            message.set("File Saved Successfully")
        else:
            message.set("Saved Canceled")
            PATH = ""

    # Configuration
    root = Tk()
    root.title(TITLE)

    #  Menú superior
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new_file)
    filemenu.add_command(label="Open", command=open_file)
    filemenu.add_command(label="Save", command=save_file)
    filemenu.add_command(label="Save as", command=save_as_file)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=root.quit)
    menubar.add_cascade(menu=filemenu, label="Archive")

    # Box of central text
    text = Text(root)
    text.pack(fill="both", expand=1)
    text.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

    #  Bottom Monitor
    message = StringVar()
    message.set("Welcome to EditorEX")
    monitor = Label(root, textvar=message, justify='left')
    monitor.pack(side="left")

    root.config(menu=menubar)
    #  Finally loop aplication
    root.mainloop()


if __name__ == '__main__':
    start()