from tkinter import *
from tkinter import filedialog


def saveFile():
    text = textArea.get("1.0", END)
    file = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text File", ".txt"), ("HTML file", ".html"), ("All Files", "*.*")],
        initialdir="F:\\python\\GUI\\",
    )

    if file is None:
        return
    file.write(text)
    file.close()


window = Tk()

btn = Button(master=window, text="Save Button", command=saveFile)
textArea = Text(master=window)

btn.pack(side="bottom")
textArea.pack()

window.mainloop()
