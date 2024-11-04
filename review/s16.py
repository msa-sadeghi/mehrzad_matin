# def f1(numbers):
#     s = 0
#     for n in numbers:
#         s += n
#     return s

# res = f1([1,2,3,4,5,6,7,8,9])
# print(res)

# res = f1([12,32,53,74,59,16,7,8,9])
# print(res)

# def f2():
#     for num in range(101, 1000,2):
#         print(num)

# f2()


# def f3(number):
#     if number % 4 == 0:
#         print("yes")
#     else:
#         print("no")
# f3(2)
# f3(4)
# f3(44)
# f3(64)


# def f4():
#     count = 0
#     while True:
#         n = int(input("enter a number: "))
#         if n <= 0:
#             break
#         count += 1
#     return count

# print(f4())

# def f5():
#     count = -1
#     n = 1
#     while n > 0:
#         n = int(input("enter a number: "))
        
#         count += 1
#     return count

# print(f5())
        
        
# def f5(a, b):
#     return a + b

# print(f5(2,3))
# print(f5(12,13))


# def f6(message):
#     return message[::-1]

# print(f6("mehrzad"))
# print(f6("matin"))
# print(f6("morteza"))

# print(type("dasdasd"))


# def f7(number):
#     for i in range(1,number):
#         if i % 2 == 0:
#             print(i)
            
# f7(5)

# def is_prime_number(n):
#     if n <= 1:
#         return False
#     res = "yes"
#     for x in range(2, n):
#         if n % x == 0:
#             res = "no"
#             break
#     return res

# for i in range(100):
#     print(f" {i} => {is_prime_number(i)}")            
         
         
import turtle
sc = turtle.Screen()
sc.bgcolor("yellow")
# sc.bgpic("wait_32.gif")
sc.title("hello")
sc.setup(700, 600)
sc.register_shape("wait_32.gif")
t = turtle.Turtle()
# t.shape("turtle") # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
t.shape("wait_32.gif")
t.pencolor("red")
t.pensize(6)
t.speed("fastest")
def draw_shape(x, y):
    sides = int(sc.numinput("sides", "enter sides :", minval=3, maxval=9))
    color = sc.textinput("color", "enter the color")
    length = int(sc.numinput("length", "enter the length :", minval=30, maxval=80))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(sides):
        t.fd(length)
        t.left(360/sides)
    t.end_fill()
sc.onclick(draw_shape)
turtle.done()