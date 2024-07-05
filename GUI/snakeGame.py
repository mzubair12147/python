from tkinter import *
import random

# configurations
WIDTH = 600
HEIGHT = 600

SPEED = 100
SPACESIZE = 25
BODYPARTS = 3
SNAKECOLOR = "green"
FOODCOLOR = "red"
BACKGROUND = "black"


class Snake:
    def __init__(self):
        self.bodySize = BODYPARTS
        self.coord = []
        self.squares = []
        for i in range(0, BODYPARTS):
            self.coord.append([0, 0])
        for x, y in self.coord:
            square = canvas.create_rectangle(
                x, y, x + SPACESIZE, y + SPACESIZE, fill=SNAKECOLOR, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, int((WIDTH / SPACESIZE) - 1)) * SPACESIZE
        y = random.randint(0, int((HEIGHT / SPACESIZE) - 1)) * SPACESIZE
        self.coord = [x, y]
        oval = canvas.create_oval(
            x, y, x + SPACESIZE, y + SPACESIZE, fill=FOODCOLOR, tag="food"
        )


def nextTurn(snake, food):
    x, y = snake.coord[0]
    if direction == "up":
        y -= SPACESIZE
    elif direction == "down":
        y += SPACESIZE
    elif direction == "left":
        x -= SPACESIZE
    elif direction == "right":
        x += SPACESIZE

    snake.coord.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y, x + SPACESIZE, y + SPACESIZE, fill=SNAKECOLOR
    )
    snake.squares.insert(0, square)

    if x == food.coord[0] and y == food.coord[1]:
        global score
        score += 1
        scoreLabel.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coord[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if checkCollision(snake) is True:
        gameOver()
    else:
        windows.after(SPEED, nextTurn, snake, food)


def changeDirection(newDirection):
    global direction

    if newDirection == "left":
        if direction != "right":
            direction = newDirection
    elif newDirection == "right":
        if direction != "left":
            direction = newDirection
    elif newDirection == "up":
        if direction != "down":
            direction = newDirection
    elif newDirection == "down":
        if direction != "up":
            direction = newDirection


def checkCollision(snake):
    x, y = snake.coord[0]
    if x < 0 or x >= WIDTH:
        return False
    elif y < 0 or y >= HEIGHT:
        return True

    for bodyPart in snake.coord[1:]:
        if x == bodyPart[0] and y == bodyPart[1]:
            print("Shit 3")
            return True

    return False


def gameOver():
    canvas.delete(ALL)
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font=("Arial", 30),
        text="Game Over",
        fill="red",
        tag="gameover",
    )


windows = Tk()
windows.title("Snake Game")

score = 0
direction = "down"

scoreLabel = Label(master=windows, text=f"Score: {score}", font=("Times New Roman", 20))
scoreLabel.pack()

canvas = Canvas(master=windows, width=WIDTH, height=HEIGHT, background=BACKGROUND)
canvas.pack()

windows.update()
windowsWidth = windows.winfo_width()
windowsHeight = windows.winfo_height()
screenWidth = windows.winfo_screenwidth()
screenHeight = windows.winfo_screenheight()

y = int((screenHeight / 2) - (windowsHeight / 2))
x = int((screenWidth / 2) - (windowsWidth / 2))

windows.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

windows.bind("<Left>", lambda event: changeDirection("left"))
windows.bind("<Up>", lambda event: changeDirection("up"))
windows.bind("<Down>", lambda event: changeDirection("down"))
windows.bind("<Right>", lambda event: changeDirection("right"))

snake = Snake()
food = Food()

nextTurn(snake, food)
windows.mainloop()
