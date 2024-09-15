import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)

assert distance(1, 2, 4, 2) == 3
assert distance(1, 2, 4, 6) == 5
assert distance(0, 0, 1, 1) == math.sqrt(2)
assert distance(1, 2, 1, 2) == 0