from tkinter import *

Wind = Tk()

Wind.geometry("400x400")


def moveUp(event):
    # label.place(x=label.winfo_x(), y=label.winfo_y() - 10)
    canvas.move(photoImage2, 0, -10)


def moveDown(event):
    # label.place(x=label.winfo_x(), y=label.winfo_y() + 10)
    canvas.move(photoImage2, 0, 10)


def moveLeft(event):
    # label.place(x=label.winfo_x() - 10, y=label.winfo_y())
    canvas.move(photoImage2, 0 - 10, 0)


def moveRight(event):
    # label.place(x=label.winfo_x() + 10, y=label.winfo_y())
    canvas.move(photoImage2, 0 + 10, 0)


Wind.bind("<W>", moveUp)
Wind.bind("<A>", moveLeft)
Wind.bind("<S>", moveDown)
Wind.bind("<D>", moveRight)

Wind.bind("<Up>", moveUp)
Wind.bind("<Left>", moveLeft)
Wind.bind("<Down>", moveDown)
Wind.bind("<Right>", moveRight)

# photoImage = PhotoImage(file="GUI\\icon.png")
# label = Label(master=Wind, image=photoImage, background="darkgray")
# label.pack()


# moving an image in canvas
canvas = Canvas(master=Wind, height=500, width=500, background="blue")
myImage = PhotoImage(file="GUI\\icon.png")
photoImage2 = canvas.create_image(0, 0, image=myImage, anchor=NW)
canvas.pack()
Wind.mainloop()
