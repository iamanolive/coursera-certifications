# modular arithmetic

num = 49
tens_digit = num // 10
print tens_digit
ones_digit = num % 10
print ones_digit
print 10 * tens_digit + ones_digit

hour = 20
shift = 8
print (hour + shift) % 24

width = 800
position = 797
move = 5
position = (position + move) % width
print position

width = 800
position = 2
move = -5
position = (position + move) % width
print position