# import random
# my_list = []
# for i in range(10):
#     my_list.append(random.randint(0,100))
# print(my_list)
# print(min(my_list))
# print(max(my_list))
    
# students = ["mehrzad", "matin", "morteza", "arash", "sara"]
# def my_function(names):
#     count = 0
#     for n in names:
#         if len(n) > 5:
#             count += 1
#     return count

# print(my_function(students)) 

# numbers = [19,1,34,56,2,10]
# even_numbers = []
# for n in numbers:
#     if n % 2 == 0:
#         even_numbers.append(n)
        
# print(even_numbers)

def my_function(number):
    res = True
    for i in range(2, number):
        if number % i == 0:
            res = False
    return res
output = []
for i in range(2, 101):
    x = my_function(i)
    if x == True:
        output.append(i)
print(output)
    