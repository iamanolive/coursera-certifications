total = 0
count = 0
while True:
    inp = input("enter a number: ")
    if inp == "done": break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print("average:", average)


numlist = list()
while True:
    inp = input("enter a number: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("average:", average)