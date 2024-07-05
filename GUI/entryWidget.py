from tkinter import *


def submit():
    text = entry.get()
    print(f"The text inside the text box is: {text}")
    entry.delete(0, END)
    entry.insert(0, "The text box is disabled")
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backSpace():
    entry.delete(len(entry.get()) - 1, END)


# entry widget : A text box that accepts a single line of user input
windows = Tk()
windows.geometry("800x500")

entry = Entry(
    master=windows,
    font=("arial", 40),
    foreground="lightblue",
    background="black",
    # to show a symbol in place of text we can use the show argument
    # show="*",
)

entry.insert(0, "Fuck You")

submitBtn = Button(
    master=windows,
    text="Submit",
    command=submit,
)

deleteBtn = Button(
    master=windows,
    text="Delete",
    command=delete,
)

backSpaceBtn = Button(
    master=windows,
    text="Back Space",
    command=backSpace,
)
entry.pack(side=LEFT)
submitBtn.pack(side=RIGHT)
deleteBtn.pack(side=RIGHT)
backSpaceBtn.pack(side=RIGHT)

windows.mainloop()
