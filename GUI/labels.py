from tkinter import *

# label : an area widget that holds text and/or an image within a window

windows = Tk()
windows.geometry("500x500")
# windows.config(background="black")
# master argument is the name of the container windows which is containing the label
# we can also pass options(keyword arguments to this label)
image = PhotoImage(file="GUI\\icon.png")
image.width()
label = Label(
    master=windows,
    text="This is a label and it is very nice",
    font=("Times New Roman", 40, "underline"),
    foreground="white",
    background="black",
    border=20,
    relief=RAISED,
    padx=20,
    pady=10,
    image=image,
    compound=LEFT,
)

# by default widget are placed at the top center of our windows
# label.pack()

# to place our widget at a different location we can use the place method and pass the coordinates to the function
label.place(x=0, y=0)

windows.mainloop()
print("program terminated")
