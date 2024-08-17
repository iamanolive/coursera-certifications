def print_digits(number):
    tens_digit = number // 10
    ones_digit = number % 10
    print "The tens digit is " + str(tens_digit) + ", and the ones digit is " + str(ones_digit) + "."
    
print_digits(42)
print_digits(99)
print_digits(5)