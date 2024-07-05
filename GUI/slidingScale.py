from tkinter import *


def display():
    print(f"The value of x is: {x.get()}")


def getTemp():
    value = scale.get()
    print(f"The temperature is: {value}")


windows = Tk()
windows.geometry("400x100")
image = PhotoImage(file="GUI\\icon.png")

x = IntVar()

# it is a placeholder. means that the x variable will store an int value in future and it is showing that it is an int variable
scale = Scale(
    master=windows,
    from_=0,
    to=100,
    length=300,
    orient=HORIZONTAL,
    tickinterval=20,  # add numeric indicators of sliders
    font=("Arial", 10),
    showvalue=TRUE,
    resolution=2,  # increment of slider,
    troughcolor="lightblue",
    foreground="#990000",
    background="darkgray",
)
btn = Button(master=windows, text="Temperature", command=getTemp)

# formula for always in middle point
scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"])

scale.pack(side=LEFT)
btn.pack()

windows.mainloop()
