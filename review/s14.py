# students = ["bababba", "aaaa", "amamamam"]
# for s in students:
#     if s[0] == "a":
#         print(s)

f = open("boys.txt")
boy_names = ()
for line in f:
    boy_names += (line.split('.')[1][:-1].strip().lower(),)
    
print(boy_names)

names = ['Ali', 'Sara', 'Reza', 'Lian', "nazanin"]
for n in names:
    if n.lower() in boy_names:
        print(f"Mr {n}")
    else:
        print(f"Ms {n}")
        
        
s = {
    "a" :"a",
    "s" : "x"
}