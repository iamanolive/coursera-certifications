hours = input("enter hours:")
rate = input("enter rate:")

hours = float(hours)
rate = float(rate)

def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return (40 * rate) + ((hours - 40) * rate * 1.5)
    

print("Pay", computepay(hours, rate))