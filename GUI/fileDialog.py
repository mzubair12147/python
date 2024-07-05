# file dialog : to open and read the content of a file

from tkinter import *
from tkinter import filedialog


def selectFile():
    # this function returns a path to the file where it is located
    path = filedialog.askopenfilename(
        initialdir="C:\\windows",
        title="Open File",
        filetypes=[("text files", "*.txt"), ("all types", "*.*")],
    )
    print(path)
    file = open(path, "r")
    for line in file:
        print(line)
    file.close()


window = Tk()

btn = Button(master=window, text="Select File", command=selectFile)
btn.pack()

window.mainloop()
