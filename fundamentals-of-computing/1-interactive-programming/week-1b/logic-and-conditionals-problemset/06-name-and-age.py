def name_and_age(name, age):
    if age < 0:
        return "Error: Invalid age."
    else:
        return name + " is " + str(age) + " years old."