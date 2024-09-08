numbers = [9, 3, 8, 11, 5, 29, 2]
best_number = numbers[0]
for number in numbers:
    if number > best_number:
        best_number = number
print(best_number)