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
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag = "snake")
            self.squares.append(square)



class Food:
    def __init__(self) -> None:
        x = randint(0, (GAME_WIDTH//SPACE_SIZE - 1)) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT//SPACE_SIZE - 1)) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag = "food")



def next_turn(snake, food):
    x,y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, [x,y])
    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0,square)
    
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score:{score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    if check_game_over(snake)   :
        game_over()
    else:
        window.after(200, next_turn, snake, food)
 
def change_direction(new_dir):
    global direction
    if new_dir == "left":
        if direction != "right":
            direction = new_dir
    elif new_dir == "right":
        if direction != "left":
            direction = new_dir
    elif new_dir == "up":
        if direction != "down":
            direction = new_dir
    elif new_dir == "down":
        if direction != "up":
            direction = new_dir


def check_game_over(snake):
    x,y = snake.coordinates[0]
    if x < 0 or x > GAME_WIDTH:
        return True
    if y < 0 or y > GAME_HEIGHT:
        return True
    for b in snake.coordinates[1:]:
        if x == b[0] and y == b[1]:
            return True
    return False
 
def game_over() :
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("arial", 60), text="GAME OVER!", fill="#DF1A2F", tag="gameover")
 
def restart() :
    print("ok")
     
direction = "down"
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

restart = Button(window, text="RESTART", fg="red", command=restart)
restart.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width/2 - window_width/2)
y = int(screen_height/2 - window_height/2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()
next_turn(snake, food)

window.bind("<Left>", lambda e:change_direction("left"))
window.bind("<Right>", lambda event:change_direction("right"))
window.bind("<Down>", lambda event:change_direction("down"))
window.bind("<Up>", lambda event:change_direction("up"))

window.mainloop()


# def my(number):
#     return number ** 2

# print(my(3))


# x = lambda number : number ** 2 
# print(x(3))