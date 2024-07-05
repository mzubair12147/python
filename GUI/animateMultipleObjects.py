from tkinter import *
import time


class Ball:
    def __init__(self, canvasArg, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvasArg
        self.image = canvasArg.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coord = self.canvas.coords(self.image)
        if coord[2] >= self.canvas.winfo_width() or coord[0] < 0:
            self.xVelocity = -self.xVelocity
        if coord[3] >= self.canvas.winfo_height() or coord[1] < 0:
            self.yVelocity = -self.yVelocity
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)


HEIGHT = 500
WIDTH = 800

window = Tk()

canvas = Canvas(master=window, height=HEIGHT, width=WIDTH, background="#dddddd")
canvas.pack()

ball1 = Ball(canvas, 0, 0, 200, 1, 1, "Blue")
ball2 = Ball(canvas, 0, 0, 100, 4, 1, "red")

while True:
    ball1.move()
    ball2.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
