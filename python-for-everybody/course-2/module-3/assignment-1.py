filename = input("enter filename: ")
filehandle = open(filename)

for line in filehandle:
    line = line.rstrip()
    print(line.upper())