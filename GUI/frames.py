# frames : a rectangular widget to group and hold widgets

from tkinter import *

windows = Tk()

frame = Frame(master=windows, background="black", border=5, relief=RAISED)

btn1 = Button(master=frame, text="W", padx=10, pady=10, font=("consolas", 16))
btn2 = Button(master=frame, text="S", padx=10, pady=10, font=("consolas", 16))
btn3 = Button(master=frame, text="A", padx=10, pady=10, font=("consolas", 16))
btn4 = Button(master=frame, text="D", padx=10, pady=10, font=("consolas", 16))

btn1.pack(side=TOP)
btn2.pack(side=LEFT)
btn3.pack(side=RIGHT)
btn4.pack(side=BOTTOM)

frame.place(x=0, y=0)
frame.pack()
windows.mainloop()
