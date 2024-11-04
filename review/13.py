# a = range(1,51)
# print(list(a))

# اعداد = [1,2,3,4,5,6,7,8,9]
# for عدد in اعداد:
#     print(عدد)
    
# for ایندکس in range(len(اعداد)):
#     print(اعداد[ایندکس])


# x = ('apple', 'banana', 'cherry')
# print(x[1])


# x = [10.1, 20, 30, 40]
# s = 0
# for number in x:
#     s += number
# print(s)


# book = {
#     "title" : "harry potter",
#     "author": "rowling",
#     "year": 2003   
# }

# book["author"] = "JK Rowling"
# book["year"] = 2004
# book.update({"author" : "JK Rowling", "year" : 2004})
# print(book)

# تاپل = ('apple', 'orange', 'grape')

# for میوه in تاپل:
#     print(میوه)

# fruits = ['apple', 'orange', 'grape']
# output = ""
# for f in fruits:
#     output += f + " "
# print(output)

# import random
# scores = []
# n = 0
# for i in range(7):
#     s = random.randint(10, 101)
#     scores.append(s)
#     if s > 60:
#         n += 1
        
# print(scores)
# print(n)

my_dict = {'apple': 100, 'banana': 50, 'orange': 75}
print(sum(my_dict.values()))


numbers = [33, 12, 45, 67, 22]
# print(max(numbers))
# print(min(numbers))
min_ = numbers[0]
for n in numbers:
    if n < min_:
        min_ = n
print(min_)

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',\
    'Friday', 'Saturday', 'Sunday')
for d in days:
    print(d, end=" ")
temperature = {'Monday': 20, 'Tuesday': 22, 'Wednesday': 19}
print()
for temp in temperature.values():
    print(temp)
    
my_list = [1, 4, 6, 8]
my_list.append(10)
print(my_list)

student_info = {
    'name' : "sara",
    'age' : 20,
    'grades' : [100, 90, 78 , 86]
}
print(student_info['grades'])
new_list = []
numbers = [2, 3, 5, 7, 11]
for n in numbers:
    new_list.append(n * n)
print(new_list)

countries = {'Iran': 85000000, 'USA': 331000000}
for c in countries:
    if countries[c] > 100_000_000:
        print(c)
        
        
x = (1,2,3)
t, b, c = (1,2,3)
print(x)
print(type(t))