file_object = open("squares.txt", "w")

for number in range(13):
    square = number * number
    file_object.write(str(square))
    file_object.write("\n")

file_object.close()


new_file_object = open("squares.txt", "r")
print(new_file_object.read()[:10])