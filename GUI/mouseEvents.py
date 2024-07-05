from tkinter import *

Wind = Tk()


def doSomething(event):
    print(f"The coordinates are: {event.x}, {event.y}")


# Button-2 scroll event
# Button-1 left mouse button event
# Button-3 right mouse button event
# Wind.bind("<Button-1>", doSomething)
# Wind.bind("<Button-2>", doSomething)
Wind.bind("<Button-3>", doSomething)

# Wind.bind("<ButtonRelease>", doSomething)
# Wind.bind("<Enter>", doSomething)  # mouse enter event
# Wind.bind("<Motion>", doSomething) # consistently gives the coordinates when the mouse move


Wind.mainloop()
