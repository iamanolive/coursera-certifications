list1 = [1, 5, 7]
total = 0
for number in list1:
    total = total + number
print(total)


def total(input_list):
    total = 0
    for number in input_list:
        total = total + number
    return total

y = total([1, 5, 7])
print(y)