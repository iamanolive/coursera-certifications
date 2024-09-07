n = input("please enter your name: ")
print("hello", n)


str_seconds = input("please enter the number of seconds you wish to convert")
total_seconds = int(str_seconds)

hours = total_seconds // 3600
seconds_still_remaining = total_seconds % 3600
minutes = seconds_still_remaining // 60
seconds_finally_remaining = seconds_still_remaining % 60

print(hours, "hours,", minutes, "minutes,", seconds_finally_remaining, "seconds")