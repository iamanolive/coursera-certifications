hours = input("enter hours:")
rate = input("enter rate per hour:")

if float(hours) <= 40:
    pay = float(hours) * float(rate)
else:
    pay = 40 * float(rate)
    pay += 1.5 * float(rate) * (float(hours) - 40)

print(pay)