fileref = open("olympics.txt", "r")

# reading the contents of file
contents = fileref.read()
print(contents[:100])
# iterating through the whole file
for line in fileref[:4]:
    print(line.strip())

# reading lines of file
lines = fileref.readlines()
print(lines[:4])
# iterating through lines
for line in lines[:4]:
    print(line.strip())

# counting characters in file
contents = fileref.read()
print(len(contents))


fileref.close()