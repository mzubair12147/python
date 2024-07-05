# way to convert the python file into an executable
# package needed pyinstaller

# command: pyinstaller -F -W -i icon.ico clockGui.py
# -F flag is to convert into one single file
# -W flag is to prevent the opening of a gui window
# -i flag is for an icon to set. but the icon should be in .ico format

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
