the_sum = 0
x = -1

while x != 0:
    x = int(input("next number: "))
    the_sum += x

print(the_sum)


def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == "Y" or answer == "N":
            valid_input = True
        else:
            print("Y for yes, N for no")
    return answer

response = get_yes_or_no("do you like lima beans?")

if response == "Y":
    print("great! they are very healthy.")
else:
    print("too bad. if cooked right, they are quite tasty.")