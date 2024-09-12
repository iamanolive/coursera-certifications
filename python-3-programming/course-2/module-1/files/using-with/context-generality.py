fname = "mydata.txt"

with open(fname, "w") as md:
    for num in range(10):
        md.write(str(num))
        md.write("\n")

with open(fname, "r") as md:
    for line in md:
        print(line)

# md.close() is made implicit