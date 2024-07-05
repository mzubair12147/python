import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def changeColor():
    color = colorchooser.askcolor(title="Pick a color")
    textArea.config(foreground=color[1])


def changeFont(*args):
    textArea.config(font=(fontName.get(), sizeBox.get()))


def saveFile():
    filePath = filedialog.asksaveasfilename(
        initialfile="Untitled.txt",
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")],
    )

    if filePath == None:
        return
    else:
        try:
            window.title(os.path.basename(filePath))
            file = open(filePath, "w")
            file.write(textArea.get(1.0, END))
        except Exception:
            showinfo(message="Coundn't save the file")
        finally:
            file.close()


def openFile():
    filePath = askopenfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )

    try:
        window.title(os.path.basename(filePath))
        textArea.delete(1.0, END)
        file = open(filePath, "r")
        textArea.insert(1.0, file.read())
    except Exception:
        showinfo(message="Couldn't read the file.")
    finally:
        file.close()


def newFile():
    title = "Untitled!"
    window.title(title)
    textArea.delete(1.0, END)


def cut():
    textArea.event_generate("<<Cut>>")


def copy():
    textArea.event_generate("<<Copy>>")


def paste():
    textArea.event_generate("<<Paste>>")


def about():
    showinfo(
        title="About",
        message="This is a shit program and do not use it. Otherwise you will get hacked.",
    )


def quit():
    window.quit()


window = Tk()

window.title("Notepad")

# centering window
windowWidth = 600
windowHeight = 400
screenHeight = window.winfo_screenheight()
screenWidth = window.winfo_screenwidth()

# calculating coordinates
x = int((screenWidth / 2) - (windowWidth / 2))
y = int((screenHeight / 2) - (windowHeight / 2))

window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

file = None
fontName = StringVar()
fontSize = StringVar()

fontName.set("Arial")
fontSize.set("20")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

textArea = Text(master=window, font=(fontName.get(), fontSize.get()))
scrollBar = Scrollbar(master=textArea)

textArea.config(yscrollcommand=scrollBar.set)
textArea.grid(sticky=N + E + S + W)
scrollBar.pack(side=RIGHT, fill=Y)

frame = Frame(master=window)
frame.grid()

colorBtn = Button(
    master=frame,
    font=(fontName.get(), fontSize.get()),
    text="Color",
    command=changeColor,
)
colorBtn.grid(row=0, column=0)

fontBox = OptionMenu(
    frame,
    fontName,
    # get all the font families in the option menu
    *font.families(),
    command=changeFont,
)
fontBox.grid(row=0, column=1)

sizeBox = Spinbox(frame, from_=1, to=100, textvariable=fontSize, command=changeFont)
sizeBox.grid(row=0, column=2)

menuBar = Menu(master=window)
window.config(menu=menuBar)

fileMenu = Menu(master=menuBar, tearoff=0)
# to make it a drop down menu
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_separator()
fileMenu.add_command(label="Open File", command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label="Save File", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(master=menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_separator()
editMenu.add_command(label="Copy", command=copy)
editMenu.add_separator()
editMenu.add_command(label="Paste", command=paste)

helpMenu = Menu(master=menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)

window.mainloop()
