import math

def smaller_root(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        print "Error: No real solutions"
        return None
    elif discriminant == 0:
        x = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
        if x1 < x2:
            return x1
        else:
            return x2