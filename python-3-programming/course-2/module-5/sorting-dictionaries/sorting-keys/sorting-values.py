L = ["E", "F", "B", "A", "D", "I", "I", "C", "B", "A", "D", "D", "E", "D"]

d = {}

for x in L:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

for x in sorted(d.keys(), key = lambda k: d[k]):
    print("{} appears {} times".format(x, d[x]))

for x in sorted(d.keys(), key = lambda k: d[k], reverse = True):
    print("{} appears {} times".format(x, d[x]))

for x in sorted(d, key = lambda k: d[k]):
    print("{} appears {} times".format(x, d[x]))