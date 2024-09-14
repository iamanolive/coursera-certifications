def longer_than_five(list_of_names):
    for name in list_of_names:
        if len(name) > 5:
            return True
    return False

list1 = ["sam", "tera", "sal", "amita"]
list2 = ["rey", "ayo", "lauren", "natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))