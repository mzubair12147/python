from tkinter import *
import random


def nextTurn(row, column):
    global playing

    if buttons[row][column]["text"] == "" and checkWinner() is False:
        if playing == players[0]:
            buttons[row][column]["text"] = playing
            if checkWinner() is False:
                playing = players[1]
                turnLabel.config(text=f"{players[1]}'s Turn")
            elif checkWinner() is True:
                turnLabel.config(text=f"{players[0]} wins")
            elif checkWinner() == "tie":
                turnLabel.config(text="Tie")
        else:
            buttons[row][column]["text"] = playing
            if checkWinner() is False:
                playing = players[0]
                turnLabel.config(text=f"{players[0]}'s Turn")
            elif checkWinner() is True:
                turnLabel.config(text=f"{players[1]} wins")
            elif checkWinner() == "tie":
                turnLabel.config(text="Tie")


def checkWinner():
    for row in range(3):
        if (
            buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
            != ""
        ):
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if (
            buttons[0][column]["text"]
            == buttons[1][column]["text"]
            == buttons[2][column]["text"]
            != ""
        ):
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif emptySpaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="orange")
        return "tie"
    else:
        return False


def emptySpaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False

    return True


def newGame():
    global playing
    playing = random.choice(players)
    turnLabel.config(text=playing)
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#f0f0f0")


window = Tk()
window.title("Tik Tak Toe")

players = ["X", "O"]

playing = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

turnLabel = Label(master=window, text=f"{playing}'s Turn", font=("Times New Roman", 20))
turnLabel.pack(side=TOP)

resetBtn = Button(
    master=window,
    text="Reset",
    font=("Times New Roman", 20, "bold"),
    command=newGame,
    background="black",
    foreground="lightgreen",
)
resetBtn.pack(side=TOP)

frame = Frame(master=window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            master=frame,
            text="",
            font=("Times New Roman", 20),
            width=5,
            height=2,
            command=lambda row=row, column=column: nextTurn(row, column),
        )
        buttons[row][column].grid(row=row, column=column)


window.mainloop()
