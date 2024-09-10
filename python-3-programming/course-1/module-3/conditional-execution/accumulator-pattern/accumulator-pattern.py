phrase = "what a wonderful day to program"
total = 0
for character in phrase:
    if character != " ":
        total = total + 1
print(total)


phrase = "what if we went to the zoo"
total = 0
for character in phrase:
    if character in ["a", "e", "i", "o", "u"]:
        total = total + 1
print(total)