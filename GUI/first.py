from tkinter import *

# widgets : GUI elements: buttons, text boxes, labels and images
# windows : serves as a container to hold or contain those widgets

# instantiating a windows
window = Tk()  # instantiate an instance of window for us
window.geometry("1000x1000")
window.title("First GUI in Python")
logo = PhotoImage(file="GUI\\icon.png")
window.iconphoto(True, logo)
window.config(background="gray")
window.mainloop()  # place window on screen and listen for events
