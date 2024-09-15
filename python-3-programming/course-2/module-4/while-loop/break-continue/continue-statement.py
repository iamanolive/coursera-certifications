x = 0

while x <= 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1

print("done with loop. x has value", str(x))


while True:
    print("this phrase will always print")
    continue
    print("does this phrase print")

print("we are done with the while loop")