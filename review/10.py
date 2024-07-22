# def my_func(n, p):
#     f = n // 9
#     c = n - f
#     return c * p

# print(my_func(10, 2))
# print(my_func(20, 2))

def my(n_coffee, p_coffee):
    t = 0
    c = 8
    while n_coffee > 0:
        n_coffee -= 1
        if c == 0:
            c = 8
        else:
            t += p_coffee
            c -= 1
    return t

print(my(10, 2))
print(my(20, 2))