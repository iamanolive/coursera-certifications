def triangle_area(x0, y0, x1, y1, x2, y2):
    a = ((x1 - x0)**2 + (y1 - y0)**2) ** 0.5
    b = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    c = ((x2 - x0)**2 + (y2 - y0)**2) ** 0.5
    s = (a + b + c) / 2
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    return area


print triangle_area(0, 0, 3, 4, 1, 1)
print triangle_area(-2, 4, 1, 6, 2, 1)
print triangle_area(10, 0, 0, 0, 0, 10)