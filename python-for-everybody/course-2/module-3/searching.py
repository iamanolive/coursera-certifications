fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From:"):
        print(line, end = "")


fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)