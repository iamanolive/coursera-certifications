numbers = range(10)
total = 0
print("**** before the for loop *****")

for number in numbers:
    total = total + number
    print("***** a new loop iteration *****")
    print("value of number:", number)
    print("value of total:", total)

print("***** end of for loop *****")
print("final total:", total)