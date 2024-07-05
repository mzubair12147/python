from tkinter import *
from tkinter import ttk

# grid geometry : geometry manager that organizes widgets in a table like structure in a parent child
# the column width depends upon the width of the largest widget that is contained in the column
windows = Tk()

firstNameLabel = Label(master=windows, text="First Name: ", width=20, background="blue")
firstNameLabel.grid(row=0, column=0)

entryFirstName = Entry(master=windows)
entryFirstName.grid(row=0, column=1)

lastNameLabel = Label(master=windows, text="Last Name: ", background="red")
lastNameLabel.grid(row=1, column=0)

entryLastName = Entry(master=windows)
entryLastName.grid(row=1, column=1)

emailLabel = Label(master=windows, text="Email: ", background="lightgreen")
emailLabel.grid(row=2, column=0)

entryEmail = Entry(master=windows)
entryEmail.grid(row=2, column=1)

submit = Button(master=windows, text="Submit")
submit.grid(row=3, column=0, columnspan=2)

windows.mainloop()
