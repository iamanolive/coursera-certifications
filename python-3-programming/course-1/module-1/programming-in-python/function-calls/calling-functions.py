def square(base):
    return base * base

def sub(num1, num2):
    return num1 - num2

print(square(3))
square(5) # does not get printed
print(sub(6, 4))
print(sub(5, 9))

print(square(3) + 2)
print(sub(square(3), square(1 + 1)))

print(square)