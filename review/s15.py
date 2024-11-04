from tkinter import *
def my_function():
    my_window.destroy()
my_window = Tk()
my_window.title("welcome app")
# my_window.geometry("1200x900")
my_window.attributes("-fullscreen", True)
my_label = Label(my_window, text="Hello every one", font=("arial", 22))
my_label.place(x=40, y=40)


label2 = Label(my_window, text="How are you today?", font=("arial", 22))
label2.pack()


exit_button = Button(my_window,padx=30,pady=40, text="خروج", command=my_function,\
    bg="green", font=("arial", 22))
exit_button.pack()
my_window.mainloop()



