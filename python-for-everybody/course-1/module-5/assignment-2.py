hours = input("enter hours:")
rate = input("enter rate per hour:")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("error: please enter numeric input")
    quit()

if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate
    pay += 1.5 * rate * (hours - 40)

print(pay)