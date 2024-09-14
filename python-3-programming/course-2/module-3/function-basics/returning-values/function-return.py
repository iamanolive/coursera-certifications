def square(x):
    y = x * x
    return y

number = 10
result = square(number)
print(number, "squared is", result)


# interrupts the function execution
def weird():
    print("here")
    return 5
    print("there")
    return 10

x = weird()
print(x)