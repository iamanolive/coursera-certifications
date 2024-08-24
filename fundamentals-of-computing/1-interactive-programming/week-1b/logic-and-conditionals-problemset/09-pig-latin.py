def pig_latin(word):
    first_letter = word[0]
    if first_letter != "a" and first_letter != "e" and first_letter != "i" and first_letter != "o" and first_letter != "u":
        result = word[1:] + first_letter + "ay"
        return result
    else:
        result = word + "way"
        return result