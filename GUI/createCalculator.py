from tkinter import *


def createButton(key):
    return Button(
        master=frame,
        text=key,
        height=4,
        width=9,
        font=35,
        command=(lambda: buttonPress(str(key))) if key != "=" else equals,
    )


def buttonPress(num):
    global equation
    equation = equation + str(num)
    label.config(text=equation)


def equals():
    try:
        global equation
        result = eval(equation)
        label.config(text=result)
    except ZeroDivisionError as e:
        label.config(text="Arithmetic Error")
    except SyntaxError as e:
        label.config(text="Syntax Error")
    finally:
        equation = ""


def clear():
    global equation
    label.config(text="")
    equation = ""


windows = Tk()

windows.title("Calculator")
windows.geometry("600x600")

equation = ""

label = Label(
    master=windows,
    textvariable=equation,
    font=("Calibri", 20),
    background="#dddddd",
    width=40,
    height=2,
)
label.pack()

frame = Frame(master=windows)

buttons = []

for i in [1, 2, 3, "+", 4, 5, 6, "-", 7, 8, 9, "*", 0, ".", "=", "/"]:
    buttons.append(createButton(i))

k = 0
for i in range(4):
    for j in range(4):
        buttons[k].grid(row=i, column=j)
        k += 1

clear = Button(master=windows, text="Clear", command=clear, height=4, width=12, font=35)
frame.pack()
clear.pack()

windows.mainloop()
