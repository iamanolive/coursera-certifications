import re

fhand = open("regex_sum_2084132.txt", "r")
contents = fhand.readlines()

total = 0
for line in contents:
    numbers = re.findall("[0-9]+", line)
    for number in numbers:
        total += int(number)

print(total)

fhand.close()