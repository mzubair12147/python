from tkinter import *
from tkinter import ttk

Wind = Tk()

#  canvas is a widget that is used to draw graphs, plots , images and etc in a window
canvas = Canvas(master=Wind, width=600, height=500)
# redLine = canvas.create_line((0, 0, 400, 400), fill="red", width=5)
# canvas.create_line((0, 400, 400, 0), fill="green", width=5)
# canvas.create_rectangle((100, 100, 300, 300), fill="purple")
# trianglePoints = (200, 100, 300, 300, 100, 300)
# canvas.create_polygon(trianglePoints, fill="yellow", outline="orange", width=4)
# # an arc is just a line between two points, we do not list points in arc but we list the amount of space that we want to draw this arc
# canvas.create_arc(0, 0, 400, 400, style=CHORD, start=0, extent=359)


# creating a pokemon ball
canvas.create_arc(0, 0, 600, 500, extent=180, fill="red", outline="black", width=5)
canvas.create_arc(
    0, 0, 600, 500, start=180, extent=180, fill="white", outline="black", width=5
)
canvas.create_oval(300 - 50, 250 - 50, 300 + 50, 250 + 50, width=5, fill="white")


# the most recently created shape will appear on the top of the others
canvas.pack()


Wind.mainloop()
