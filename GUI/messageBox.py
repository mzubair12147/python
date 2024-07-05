from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(message="You have a virus in your machine", title="This is an alert")
    # messagebox.showwarning(message="You have a virus in your machine")
    # messagebox.showerror(message="You have a virus in your machine")
    # if messagebox.askokcancel(title="ask ok cancel", message="Do you wanna fuck"):
    #     messagebox.showinfo(message="you are fucking")
    # else:
    #     messagebox.showinfo(message="You are not fucking")

    # if messagebox.askyesno(title="ask ok cancel", message="Do you wanna fuck"):
    #     messagebox.showinfo(message="you are fucking")
    # else:
    #     messagebox.showinfo(message="You are not fucking")

    # answer = messagebox.askquestion(
    #     title="asking question", message="Do you like blowjob?: "
    # )
    # if answer == "yes":
    #     messagebox.showinfo(message="take off your pants")
    # else:
    #     messagebox.showinfo(message="let it go.")
    answer = messagebox.askyesnocancel(
        title="asking question",
        message="Do you like blowjob?: ",
        icon="warning",
    )
    if answer == "yes":
        messagebox.showinfo(message="take off your pants")
    elif answer == "no":
        messagebox.showinfo(message="let it go.")
    else:
        messagebox.showinfo(message="Fuck off")


windows = Tk()

btn = Button(master=windows, text="Click Me", command=click)
btn.pack()

windows.mainloop()
