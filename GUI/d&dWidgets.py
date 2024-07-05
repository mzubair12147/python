from tkinter import *

Wind = Tk()

Wind.geometry("400x400")


def startMove(event):
    label.startX = event.x
    label.startY = event.y


def Moving(event):
    x = label.winfo_x() - label.startX + event.x
    y = label.winfo_y() - label.startY + event.y
    label.place(x=x, y=y)


label = Label(master=Wind, width=10, height=5, background="blue")
label.place(x=0, y=0)
label.bind("<Button-1>", startMove)
label.bind("<B1-Motion>", Moving)

label.pack()
Wind.mainloop()
