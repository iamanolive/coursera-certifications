initial = 7

def f1(x, y = 3, z = initial):
    print("x is", str(x))
    print("y is", str(y))
    print("z is", str(z))

f1(x = 2)
f1(x = 2, z = 8)
f1(z = 8, x = 20)
f1(10, z = 8)