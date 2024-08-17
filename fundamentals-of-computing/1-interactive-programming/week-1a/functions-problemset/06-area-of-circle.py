import math

def circle_area(radius):
    PI = math.pi
    area = PI * (radius ** 2)
    return area

print circle_area(8)
print circle_area(3)
print circle_area(12.9)