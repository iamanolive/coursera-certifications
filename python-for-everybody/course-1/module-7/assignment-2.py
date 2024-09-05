largest = None
smallest = None

while True:
    is_number = True
    number = input("enter a number: ")
    
    if number == "done":
        break

    try:
        number = int(number)
    except:
        print("Invalid input")
        is_number = False
    
    if is_number == True and largest is None:
        largest = number
    elif is_number == True and number > largest:
        largest = number
    if is_number == True and smallest is None:
        smallest = number
    elif is_number == True and number < smallest:
        smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)