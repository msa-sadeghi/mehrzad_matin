def register(user_name, password, family):
    with open("users.txt", "a") as f:
        f.write(f"{user_name},{family},{password}")
        f.write("\n")
        
def login(user_name, password):
    is_valid = False
    with open("users.txt", "r") as f:
        for person in f.read().strip().split("\n"):
            person_info = person.split(",")
            if person_info[0] == user_name:
                if person_info[2] == password:
                    is_valid = True
                    break
        if is_valid ==True:
            show_profile()
        else:
            print("username or password is not correct")
            
def show_profile():
    print("WELCOME")
    
user_input = input("login -> 0 | register -> 1 ? ")
if user_input == "0":
    user_name = input("enter the username: ")
    password = input("enter the password: ")
    login(user_name, password)
elif user_input == "1":
    user_name = input("enter the username: ")
    family = input("enter the family: ")
    password = input("enter the password: ")
    register(user_name, password, family)
    
