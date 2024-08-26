def format_time(seconds):
    minutes = seconds / 100
    seconds = seconds % 100
    return str(minutes) + " minutes and " + str(seconds) + " seconds"


print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)