# x = []
# n = int(input("how many numbers you want? "))
# for i in range(n):
#     a = int(input("enter a number: "))
#     x.append(a)

# x.sort()
# print("minimum",x[0])
# print("maximum",x[-1])

# x = [28, 25, 42, 2, 28]
# x = []
# n = int(input("how many numbers you want? "))
# for i in range(n):
#     a = int(input("enter a number: "))
#     x.append(a)

# def getSmallest(my_list):
#     minimum = my_list[0]
#     for number in my_list:
#         if number < minimum:
#             minimum = number
#     return minimum

# print(getSmallest(x))


# def calculateSum(my_list):
#     a = 0
#     for number in my_list:
#         a += number
#     return a
# print(calculateSum([2, 4, 6, 8, 10]))
    
    
    


# def median(x):
#     if len(x) == 0:
#         return None
#     median_index = len(x) // 2
#     if len(x) % 2 == 0:
#         return (x[median_index] + x[median_index - 1]) / 2
#     return x[median_index]

# print(median([1,2,3]))
# print(median([1,2,3,4]))


names = ["artin", "nikan", "armin", "armin","nikan", "artin", "nikan","nikan", "arman","armin"]
name_count = {}
name_res = ""
c = 0

for n in names:
    if n in name_count:
        name_count[n] += 1
    else:
        name_count[n] = 1
    if name_count[n] > c:
        c = name_count[n]
        name_res = n
all_names = []       
for item in name_count.items():
    if item[1] == c:
        all_names.append(item[0])
print(all_names)
    