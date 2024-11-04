# scores = []

# for i in range(4):
#     sc = float(input(f"enter score #{i+1}: "))
#     scores.append(sc)
# print(scores)
# for i in range(4):
#     scores[i] += 2
#     if scores[i] > 20:
#         scores[i] = 20
    
# print(scores)

# x = (1,)

# x += (2,)
# print(x)
# x = tuple()
# print(type(x))
scores = ()
for i in range(4):
    s = float(input("enter score: "))
    scores += (s,)
print(scores)