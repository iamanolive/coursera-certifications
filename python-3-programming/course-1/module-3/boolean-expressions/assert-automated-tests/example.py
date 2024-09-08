lst = ["a", "b", "c"]

first_type = type(lst[0])
for item in lst:
    assert type(item) == first_type

lst2 = ["a", "b", "c", 17]
first_type = type(lst2[0])
for item in lst2:
    assert type(item) == first_type

lst = ["a", "b", "c"]
assert len(lst) < 10