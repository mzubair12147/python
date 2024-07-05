# frames : a rectangular widget to group and hold widgets

from tkinter import *


def createWindows():
    # Tk() is a new independent windows and is not linked with any other windows
    # new_windows = Toplevel(master=windows)  # top level: new windows on top of other windows, linked to a bottom window
    new_windows = Toplevel()
    print("SHIT")


windows = Tk()

create = Button(
    master=windows,
    text="Create a new window",
    padx=10,
    pady=10,
    font=("consolas", 16),
    command=createWindows,
)
create.pack()

windows.mainloop()
