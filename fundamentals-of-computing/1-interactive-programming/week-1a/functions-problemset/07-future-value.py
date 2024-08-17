def future_value(present_value, annual_rate, years):
    f_value = present_value * (1 + (0.01 * annual_rate)) ** years
    return f_value

print future_value(1000, 7, 10)
print future_value(200, 4, 5)
print future_value(1000, 3, 20)