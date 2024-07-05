from tkinter import *
from tkinter import filedialog


def openFile():
    path = filedialog.askopenfile()


def saveFile():
    path = filedialog.asksaveasfile()


def exit():
    windows.quit()


def editFile():
    pass


windows = Tk()
windows.geometry("400x100")
# image = PhotoImage(file="GUI\\icon.png")

menuBar = Menu(master=windows, font=("PP Mori", 12))
fileMenu = Menu(master=menuBar, tearoff=0, font=("PP Mori", 12))
editMenu = Menu(master=menuBar, tearoff=0, font=("PP Mori", 12))

windows.config(menu=menuBar)

menuBar.add_cascade(label="file", menu=fileMenu)
fileMenu.add_command(labe="open", command=openFile)
fileMenu.add_separator()
fileMenu.add_command(labe="save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(labe="exit", command=exit)

menuBar.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="cut")
editMenu.add_separator()
editMenu.add_command(label="copy")
editMenu.add_separator()
editMenu.add_command(label="paste")


windows.mainloop()
