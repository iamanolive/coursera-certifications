def total_seconds(hours, minutes, seconds):
    t_seconds = hours * 3600
    t_seconds += minutes * 60
    t_seconds += seconds
    return t_seconds

print total_seconds(7, 21, 37)
print total_seconds(10, 1, 7)
print total_seconds(1, 0, 1)