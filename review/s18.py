from tkinter import *

GAME_WIDTH = 700
GAME_HEIGHT = 700
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