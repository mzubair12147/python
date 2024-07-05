from tkinter import *

# text widget is a widget in which we can type multiple lines of text i
window = Tk()


def submitText():
    text = textArea.get("1.0", END)
    print(text)


textArea = Text(
    master=window,
    background="black",
    foreground="white",
    font=("Ink free", 25),
    height=8,
    width=20,
    padx=20,
    pady=20,
)
textArea.pack()

submitBtn = Button(
    master=window,
    text="Submit",
    command=submitText,
)
submitBtn.pack()

window.mainloop()
