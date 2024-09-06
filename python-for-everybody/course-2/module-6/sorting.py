d = {"a": 10, "c": 22, "b": 1 }
print(d.items())

print(sorted(d.items()))
print(d.items())


# sorting by key
d = {"b": 1, "c": 22, "a": 10}
t = sorted(d.items())
print(t)
for k, v in sorted(d.items()):
    print(k, v)


# sorting by value
c = {"a": 10, "b": 1, "c": 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse = True)
print(tmp)


# list comprehension
c = {"a": 10, "b": 1, "c": 22}
print(sorted( [(v, k) for k, v in c.items()] ))