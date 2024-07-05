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