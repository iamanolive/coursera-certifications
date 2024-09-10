x = 3
y = 4

if x < y:
    z = x
else:
    if x > y:
        z = y
    else:
        assert x == y
        z = 0

print(z)