# the upper method
first_string = "Hello World"
print(first_string.upper())
# the lower method
second_string = first_string.lower()
print(first_string, second_string)


# the strip method
first_string = "   Hello, world   "
count_of_l = first_string.count("l")
print(count_of_l)
print("***" + first_string.strip() + "***")
# the replace method
new_string = first_string.replace("o", "***")
print(new_string)