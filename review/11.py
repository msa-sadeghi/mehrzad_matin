# myfile = open("test", "w")

# print("hello", "friends", "!", sep="-", end="-", file=myfile)
# print("how are you today", file=myfile)
# import time
# message = "hello friends."
# for c in message:
#     print(c, end="", flush=True)
#     time.sleep(0.2)

# r = float(input("enter a radius: "))
# print(f"a: {3.14 * r ** 2}")
# print(f"p: {3.14 * r * 2}")

x = 0
y = 11
while y:
    y %= 10
    print(y)
    break
    x += 1
    
print(x)
    