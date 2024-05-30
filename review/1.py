username = input("enter the username ")
password = input("enter the password ")

if username == "root" and password == "123456":
    print("welcome", username)
else:
    print("username or password is not correct")