# string literals
s1 = "Rixner's funny"
s2 = "Warren wears nice ties!"
s3 = " t-shirts!"
print s1, s2, s3

# combining strings
s4 = "Warren" + " and " + "Rixner" + " are nuts!"
print s4

# characters and slices
print s1[0]
print s1[1]
print s1[2]
print s1[-1] # last character
print s1[-2]

print len(s1) # string length

print s1[0:7] # upto but not including 7
print s1[0:8]
print s1[0:6] + s2[6:]
print s2[:13] + s1[9:] + s3

# converting strings
s5 = str(375)
print s5
print s5[1:]
i1 = int(s5[1:])
print i1
print i1 + 23


# handling single quantities
def convert_units(value, name):
    result = str(value) + " " + name
    if value > 1:
        result = result + "s"
    return result

# converting into dollars and cents
def convert(value):
    # split value into dollars and cents
    dollars = int(value)
    cents = round(100 * (value - dollars))
    # convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")
    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
    
print convert(11.23)
print convert(1.12)