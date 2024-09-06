# the .split() method
abc = "with three words"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)

# treats multiple spaces as single space
line = "a lot          of space"
etc = line.split()
print(etc)

line = "first;second;third"
thing = line.split()
print(thing)
print(len(thing))

# specifying delimiter
thing = line.split(";")
print(thing)
print(len(thing))