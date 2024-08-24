def interval_intersect(a, b, c, d):
    if c >= a and c <= b:
        return True
    elif d >= a and d <= b:
        return True
    elif a >= c and a <= d:
        return True
    elif b >= c and b <= d:
        return True
    else:
        return False