def point_distance(x0, y0, x1, y1):
    distance = ((x0 - x1)**2 + (y0 - y1)**2) ** 0.5
    return distance

print point_distance(2, 2, 5, 6)
print point_distance(1, 1, 2, 2)
print point_distance(0, 0, 3, 4)