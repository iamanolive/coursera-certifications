f = open("scarlet.txt", "r")
txt = f.read()

t_count = 0
s_count = 0

for c in txt:
    if c == "t":
        t_count += 1
    elif c == "s":
        s_count += 1

print("t:", t_count, "occurrences")