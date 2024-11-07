from tkinter import *
is_clicked = False
def myfunction():
    global is_clicked
    if is_clicked == False:
        password_entry.config({"show":""})
        is_clicked = True
    else:
        password_entry.config({"show":"*"})
        is_clicked = False


main_window = Tk()
main_window.geometry("240x130")
username_frame = Frame(main_window)
username_frame.pack(pady=10,anchor="w")

Label(username_frame, text="username").pack(side=LEFT, padx=4)
username_entry = Entry(username_frame)
username_entry.pack(side=RIGHT)

password_frame = Frame(main_window)
password_frame.pack(anchor="w")
Label(password_frame, text="password").pack(side=LEFT, padx=4)
password_entry = Entry(password_frame, show="*")
password_entry.pack(side=LEFT)

Button(password_frame, text="show", command=myfunction).pack(side=LEFT)

# TODO lambda

main_window.mainloop()