from tkinter import *

Wind = Tk()


def doSomething(event):
    keyLabel.config(text=event.keysym)


# window.bind(event,function)
Wind.bind("<Key>", doSomething)

keyLabel = Label(master=Wind, height=10, width=20, font=("PP Mori", 25))
keyLabel.pack()

Wind.mainloop()
