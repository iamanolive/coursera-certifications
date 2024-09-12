file_connection = open("olympics.txt", "r")
lines = file_connection.readlines()

for line in lines[:6]:
    print(line.strip())

header = lines[0]
field_names = header.strip().split(",")
print(field_names)

for row in lines[1:]:
    values = row.strip().split(",")
    if values[5] != "NA":
        print("{}: {}; {}".format(values[0], values[4], values[5]))