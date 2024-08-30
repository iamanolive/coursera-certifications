fname = "mbox-short.txt"
fhand = open(fname)

hours = list()

for line in fhand:
    if len(line) > 5 and line.startswith("From"):
        words = line.split()
        if len(words) == 7:
            time = words[5].split(":")
            hours.append(time[0])

counts = dict()

for hour in hours:
    counts[hour] = counts.get(hour, 0) + 1

for key, value in sorted(counts.items()):
    print(key, value)