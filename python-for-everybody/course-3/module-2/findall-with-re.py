import re
x = "my 2 favorite numbers are 19 and 12"
y = re.findall("[0-9]+", x)
print(y) # one or more digits
y = re.findall("[AEIOU]+", x)
print(y) # one or more uppercase vowels