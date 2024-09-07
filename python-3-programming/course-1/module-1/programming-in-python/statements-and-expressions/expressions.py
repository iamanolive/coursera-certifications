print(1 + 1 + (2 * 3))
print(len("hello"))


x = 3.14
y = len("hello")
print(x, y)
print(2 * len("hello") + len("goodbye"))


def square(number):
    return number * number
def sub(number1, number2):
    return number1 - number2

x = 2; y = 1
print(square(y + 3))
print(square(y + square(x)))
print(sub(square(y), square(x)))