from tkinter import *

food = ["option 1", "option 2", "option 3"]


def order():
    print(f"you ordered {x.get()}")


windows = Tk()
windows.geometry("500x600")
image = PhotoImage(file="GUI\\icon.png")

x = StringVar()

for i in food:
    radioBtn = Radiobutton(
        text=i,
        master=windows,
        variable=x,  # group radio buttons together if they share the same variable
        value=i,  # assigns each radio button a different value
        indicatoron=0,  # eliminate circle indicators
        command=order,
        font=("Impact", 20),
        foreground="darkblue",
        background="#eeeeee",
        activeforeground="#eeeeee",
        activebackground="darkblue",
        padx=20,
        pady=20,
        image=image,
        compound=RIGHT,
        width=400,  # can set the width of the buttons
    )
    radioBtn.pack(anchor=S)

windows.mainloop()
