f = open("scarlet.txt", "r")
txt = f.read()

x = {}

for c in txt:
    if c not in x:
        x[c] = 0
    x[c] += 1

letter_values = {
    "a": 1, "b": 3, "c": 3, "d": 2,
    "e": 1, "f": 4, "g": 2, "h": 4,
    "i": 1, "j": 8, "k": 5, "l": 1, 
    "m": 3, "n": 1, "o": 1, "p": 3, 
    "q": 10, "r": 1, "s": 1, "t": 1,
    "u": 1, "v": 8, "w": 4, "x": 8,
    "y": 4, "z": 10
}

scrabble_score = 0
for letter in x:
    if letter in letter_values:
        scrabble_score += letter_values[letter] * x[letter]
