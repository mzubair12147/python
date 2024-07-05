from tkinter import *


def submit():
    # selection = listBox.get(listBox.curselection())
    # print("Selected " + selection)
    items = []
    for index in listBox.curselection():
        items.insert(index, listBox.get(index))
    for item in items:
        print("You selected " + item)
    listBox


def add():
    listBox.insert(listBox.size(), entryBox.get())
    listBox.config(height=listBox.size())
    entryBox.delete(0, END)


def delete():
    # listBox.delete(listBox.curselection())
    # listBox.config(height=listBox.size())
    for index in reversed(listBox.curselection()):
        listBox.delete(index)


# list box is a listing of selectable items within it's own container
windows = Tk()
# windows.geometry("750x500")
# image = PhotoImage(file="GUI\\icon.png")

listBox = Listbox(
    master=windows,
    background="#f7ffde",
    font=("constantia", 20),
    width=20,
    selectmode=MULTIPLE,
)

# we have to add selectable text items in the listbox.
listBox.insert(0, "Item 1")
listBox.insert(1, "Item 2")
listBox.insert(2, "Item 3")
listBox.insert(3, "Item 4")

listBox.pack()

entryBox = Entry(master=windows)
entryBox.pack()

btn = Button(master=windows, text="Submit", command=submit)
addBtn = Button(master=windows, text="add Item", command=add)
deleteBtn = Button(master=windows, text="delete Item", command=delete)

btn.pack()
addBtn.pack()
deleteBtn.pack()

windows.config(height=listBox.size())
windows.mainloop()
