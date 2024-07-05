from tkinter import *
from time import *

window = Tk()


def updateTime():
    timeString = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeString)

    dayLabel.config(text=strftime("%A"))
    dateLabel.config(text=strftime("%B %d, %Y"))
    timeLabel.after(1000, updateTime)


timeLabel = Label(
    master=window, font=("arial", 25), foreground="white", background="black"
)
timeLabel.pack()

dayLabel = Label(
    master=window, font=("arial", 25), foreground="white", background="black"
)
dayLabel.pack()

dateLabel = Label(
    master=window, font=("arial", 25), foreground="white", background="black"
)
dateLabel.pack()

updateTime()

window.mainloop()
