# f = open("myfile1", "w")
# while True:
#     name = input("enter a name: ")
#     f.writelines([name, "\n"])
#     if input("do you want to quit(y or n)? ") == "y":
#         break
# f.close()

from tkinter import *

def myprint():
    f = open("myfile2", "a")
    f.writelines([name_var.get(), "\n"])
    f.close()
    name_var.set("")
    
root = Tk()
root.geometry("420x250")
frame1 = Frame(root)
frame1.pack(pady=10, anchor="w")
name_var = StringVar()
Label(frame1, text="username", bg="silver", \
    fg="blue", font=("arial", 16)).pack(side=LEFT)
name_entry = Entry(frame1,text="نام", \
bg="silver", fg="blue", font=("arial", 16), \
        textvariable=name_var, width=17)
name_entry.pack(side=RIGHT, padx=50)

frame2 = Frame(root)
frame2.pack(pady=10, anchor="w")
name_var = StringVar()

Label(frame2, text="password", bg="silver", \
    fg="blue", font=("arial", 16)).pack(side=LEFT)
password1 = Entry(frame2,text="نام", bg="silver", \
    fg="blue", font=("arial", 16),show="*", \
        textvariable=name_var, width=17)
password1.pack(side=RIGHT, padx=50)

frame3 = Frame(root)
frame3.pack(pady=10, anchor="w")
name_var = StringVar()

Label(frame3, text="Re-password", bg="silver", \
    fg="blue", font=("arial", 16)).pack(side=LEFT)
password2 = Entry(frame3,text="نام", bg="silver", \
    fg="blue", font=("arial", 16),show="*", \
        textvariable=name_var, width=17)
password2.pack(side=RIGHT, padx=17)

submit_btn = Button(root, text="register", \
    bg="silver", fg="blue", font=("arial", 16), command=myprint)
submit_btn.pack()



root.mainloop()