x = ("glenn", "sally", "joseph")
print(x[2])

y = (1, 9, 2)
print(y)
print(max(y))

for iterable in y:
    print(iterable)

# assignment using tuples
(x, y) = (4, "fred")
(a, b) = (99, 98)


# list of tuples
d = dict()
d["csev"] = 2
d["cwen"] = 4
tups = d.items()
print(tups)


# tuples are comparable
print((0, 1, 2) < (5, 1, 2))
print((0, 1, 2000000) < (0, 3, 4))
print(("jones", "sally") < ("jones", "sam"))
print(("jones", "sally") > ("adams", "sam"))