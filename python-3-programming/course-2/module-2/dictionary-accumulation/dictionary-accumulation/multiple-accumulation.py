f = open("scarlet.txt", "r")
txt = f.read()

x = {}

for c in txt:
    if c not in x:
        x[c] = 0
    x[c] += 1

print("t:", str(x["t"]), "occurrences")
print("s:", str(x["s"]), "occurrences")
print("a:", str(x["a"]), "occurrences")
print("b:", str(x["b"]), "occurrences")