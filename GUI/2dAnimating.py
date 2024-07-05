from tkinter import *
import time

HEIGHT = 600
WIDTH = 600
xVelocity = 7
yVelocity = 10

window = Tk()

window.geometry("600x600")

canvas = Canvas(master=window, height=HEIGHT, width=WIDTH, background="blue")
canvas.pack()

photo = PhotoImage(file="GUI\\icon.png")

myImage = canvas.create_image(0, 0, image=photo, anchor=NW)

image_width = photo.width()
image_height = photo.height()

while True:
    coord = canvas.coords(myImage)
    canvas.move(myImage, xVelocity, yVelocity)
    window.update()
    time.sleep(0.1)

window.mainloop()
