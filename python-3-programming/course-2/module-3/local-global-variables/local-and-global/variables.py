def square(x):
    # y has local scope
    y = x * x
    return y

# z has global scope
z = square(10)
print(z)
# print(y) throws an error


y = 5

def square(x):
    y = x * x
    return y

z = square(10)
print(z, y)


def square(x):
    global y
    w = y + 1
    y = x * x
    return y

y = 5
z = square(10)
print(y, z)