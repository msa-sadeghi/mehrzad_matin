# class Player:
#     def __init__(self, name,normal_speed) -> None:
#         self.inform = {
#                 'name' : name,
#                 'normal_speed' : normal_speed,
#                 'boost_speed' : 30,
#                 'heart' : 5,
#                 'ammo' : 13,
#         }
#     def jump(self):
#         ""

# p1 = Player("mario", 20)
# print(p1.inform['name'])
# print(p1.inform['normal_speed'])
# p2 = Player("li", 24)
# print(p2.inform['name'])
# print(p2.inform['normal_speed'])
# person = {}
# for i in range(3):
#     name = input("name:> ")
#     age = int(input("age:> "))
#     person[name] = age
# print(person)
# n = input("name:> ")
# print(person[n])
# print(person.popitem())


# digits = "0123456789"
# voroudi = input("enter a number: ")
# res = None
# for y in voroudi:
#     if y not in digits:
#         print("you must enter a number")
#         res = True
#         break
# if res == None:  
#     print(voroudi[-1])

name = input(":> ")
print(name[len(name)//2])
