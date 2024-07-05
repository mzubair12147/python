from tkinter import *
from tkinter import colorchooser  # it is a submodule


def clickMe():
    window.config(background=(colorchooser.askcolor())[1])


window = Tk()
window.geometry("200x200")
btn = Button(master=window, text="Click Me", command=clickMe)
btn.pack()
window.mainloop()
