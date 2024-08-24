def print_digits(number):
    if number < 0:
        print "Error: Input is not a two-digit number."
        return None
    elif number >= 100:
        print "Error: Input is not a two-digit number."
        return None
    else:
        tens_digit = number // 10
        ones_digit = number % 10
        print "The tens digit is " + str(tens_digit) + ", and the ones digit is " + str(ones_digit) + "."