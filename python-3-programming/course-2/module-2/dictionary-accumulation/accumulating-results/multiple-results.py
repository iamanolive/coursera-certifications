f = open("scarlet.txt", "r")
txt = f.read()

letter_counts = {}

for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] += 1

print("there are", letter_counts["t"], "ts")
print("there are", letter_counts["a"], "as")

for letter in letter_counts:
    print("there are", letter_counts[letter], letter, "s")