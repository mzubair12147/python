from tkinter import *
from tkinter import ttk

windows = Tk()

notebook = ttk.Notebook(
    master=windows
)  # a widget that managed a collection of windows and displays

tab1 = Frame(master=notebook)
tab2 = Frame(master=notebook)

label1 = Label(master=tab1, text="This is tab 1", width=50, height=20)
label2 = Label(master=tab2, text="This is tab 2", width=50, height=20)

label1.pack()
label2.pack()

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack(expand=TRUE, fill="both")  # expand to fill any space and not otherwise
# fill : fill space on x and y axis
windows.mainloop()
