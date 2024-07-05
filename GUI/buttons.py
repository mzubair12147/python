from tkinter import *


def clickMe():
    print("The button is clicked.")


windows = Tk()
windows.geometry("750x500")
image = PhotoImage(file="GUI\\icon.png")

# we can pass a call back function into the button by passing the compound parameter
btn = Button(
    master=windows,
    text="Click my butt",
    font=("calibri", 40),
    command=clickMe,
    image=image,
    compound=BOTTOM,
    foreground="darkblue",
    background="lightblue",
    activeforeground="lightblue",
    activebackground="darkblue",
    # prevent someone to click on the button
    # state=DISABLED,
)

btn.pack()
windows.mainloop()
