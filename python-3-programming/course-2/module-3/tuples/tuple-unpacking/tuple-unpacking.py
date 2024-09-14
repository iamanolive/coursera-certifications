julia = "julia", "roberts", 1967, "duplicity", 2009, "actress", "atlanta, georgia"
name, surname, birth_year, movie, movie_year, profession, birth_place = julia


a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)


def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # unpack z
# print(add(z))

print(add((3, 4), (3, 4)))


d = {"k1": 3, "k2": 7, "k3": "some other value"}
for key, value in d.items():
    print("key: {}, value: {}".format(key, value))