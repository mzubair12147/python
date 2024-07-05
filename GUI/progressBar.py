from tkinter import *
from tkinter import ttk
import time


def download():
    tasks = 100
    x = 0
    while x < tasks:
        progress["value"] += 1
        x += 1
        Wind.update_idletasks()
        time.sleep(0.01)
        percent.set(str(int((x / tasks) * 100)) + " %")


Wind = Tk()
percent = StringVar()

progress = ttk.Progressbar(master=Wind, orient=HORIZONTAL, length=400)
progress.pack()

labelPercent = Label(master=Wind, textvariable=percent)
labelPercent.pack()

btn = Button(master=Wind, text="Download", command=download)
btn.pack()
Wind.mainloop()
