fruit = ["banana", "apple", "cherry"]

# changing values of list items
fruit[0] = "pear"; print(fruit)
fruit[-1] = "orange"; print(fruit)


# changing values using slicing
alist = ["a", "b", "c", "d", "e", "f"]
alist[1:3] = ["x", "y"]; print(alist)
alist[1:3] = [] # deleting list items
print(alist)