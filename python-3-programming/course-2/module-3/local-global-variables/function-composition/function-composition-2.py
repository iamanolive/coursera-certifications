def most_common_letter(string):
    frequencies = count_frequencies(string)
    return best_key(frequencies)


def count_frequencies(string):
    d = {}
    for c in string:
        if c not in d:
            d[c] = 0
        d[c] = d[c] + 1
    return d


def best_key(dictionary):
    keys = dictionary.keys()
    best_key_so_far = list(keys)[0]
    for key in keys:
        if dictionary[key] > dictionary[best_key_so_far]:
            best_key_so_far = key
    return best_key_so_far


print(most_common_letter("ahdjgsdkssh"))