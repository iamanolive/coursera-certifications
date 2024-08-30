# the while loop
n = 5
while n > 0:
    print(n)
    n = n - 1
print("blastoff!")
print(n)

# breaking out of a loop
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("done!")

# finishing iteration with continue
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("done!")