my_list = []

# the append() method
my_list.append(5)
my_list.append(27)
my_list.append(3)
my_list.append(12)
print(my_list)

# the insert() method
my_list.insert(1, 12)
print(my_list)

# the count() method
count_of_12 = my_list.count(12)
print(count_of_12)
count_of_5 = my_list.count(5)
print(count_of_5)

# the index() method
index_of_3 = my_list.index(3)
print(index_of_3)

# the reverse() method
print(my_list)
my_list.reverse()
print(my_list)

# the sort() method
print(my_list)
my_list.sort()
print(my_list)

# the remove() method
my_list.remove(5)
print(my_list)

# the pop() method
last_item = my_list.pop()
print(last_item, my_list)