greet = "Hello, bob"

# the .lower() method
zap = greet.lower()
print(zap, greet)
print("Hi There".lower())

# the .find() method
fruit = "banana"
position = fruit.find("na")
print(position)
aa = fruit.find("z")
print(aa)

# the .upper() method
greet = "Hello Bob"
nnn = greet.upper()
print(nnn, greet)
www = greet.lower()
print(www, greet)

# the .replace() method
greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")
print(nstr)
nstr = greet.replace("o", "X")
print(nstr)

# stripping whitespace
greet = "   Hello Bob  "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# the .startswith() method
line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("p"))