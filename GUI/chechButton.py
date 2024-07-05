from tkinter import *


def display():
    print(f"The value of x is: {x.get()}")


windows = Tk()
windows.geometry("400x100")
image = PhotoImage(file="GUI\\icon.png")

x = IntVar()

# it is a placeholder. means that the x variable will store an int value in future and it is showing that it is an int variable
checkBtn = Checkbutton(
    text="I agree to something",
    master=windows,
    variable=x,
    onvalue=10,
    offvalue=0,
    command=display,
    font=("Arial", 20),
    foreground="darkblue",
    background="#eeeeee",
    activeforeground="#eeeeee",
    activebackground="darkblue",
    padx=20,
    pady=20,
    image=image,
    compound=RIGHT,
)
checkBtn.pack()

windows.mainloop()
