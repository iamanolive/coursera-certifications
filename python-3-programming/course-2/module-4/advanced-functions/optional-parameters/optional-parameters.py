def f1(x, y, z):
    print("x is", str(x))
    print("y is", str(y))
    print("z is", str(z))

f1(2, 5, 8)


def f2(x, y, z = 7):
    print("x is", str(x))
    print("y is", str(y))
    print("z is", str(z))

f2(2, 5); f2(2, 5, 9)


initial = 7

def f3(x, y = 3, z = initial):
    print("x is", str(x))
    print("y is", str(y))
    print("z is", str(z))

f3(2); f3(2, 5); f3(2, 5, 8)


initial = 7

def f3(x, y = 3, z = initial):
    print("x is", str(x))
    print("y is", str(y))
    print("z is", str(z))

initial = 10

f3(2)