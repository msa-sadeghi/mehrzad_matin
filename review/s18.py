from tkinter import *
from random import randint
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        
        for i in range(BODY_SIZE):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)



class Food:
    def __init__(self) -> None:
        x = randint(0, (GAME_WIDTH//SPACE_SIZE - 1)) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT//SPACE_SIZE - 1)) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag = "food")

GAME_WIDTH = 700
GAME_HEIGHT = 700
BODY_SIZE = 2
SPACE_SIZE = 50
SNAKE_COLOR = "yellow"
FOOD_COLOR = "red"
score = 0
window = Tk()
window.title("Snake")
window.resizable(False, False)
label = Label(window, text=f"Score: {score}", font=("Courier", 30))
label.pack()

canvas = Canvas(window, bg="black", height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

restart = Button(window, text="RESTART", fg="red")
restart.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width/2 - window_width/2)
y = int(screen_height/2 - window_height/2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()