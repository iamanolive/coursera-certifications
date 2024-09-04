x = 0
if x < 2:
    print("small")
elif x < 10:
    print("Medium")
else:
    print("LARGE")
print("all done")

# without an else block
x = 5
if x < 2:
    print("small")
elif x < 10:
    print("medium")
print("all done")

# multiple elif statements
if x < 2:
    print("small")
elif x < 10:
    print("medium")
elif x < 20:
    print("big")
elif x < 40:
    print("large")
elif x < 100:
    print("huge")
else:
    print("ginormous")