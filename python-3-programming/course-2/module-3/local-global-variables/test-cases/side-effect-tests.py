def update_counts(letters, counts_d):
    for letter in letters:
        if letter in counts_d:
            counts_d[letter] += 1
        else:
            counts_d[letter] = 1
        

counts = {"a": 3, "b": 2}
update_counts("aaab", counts)
assert counts["a"] == 6
assert counts["b"] == 3

counts = {}
update_counts("aaab", counts)
assert counts["a"] == 3
assert counts["b"] == 1

counts = {"a": 3, "b": 2}
update_counts("", counts)
assert counts["a"] == 3
assert counts["b"] == 2

counts_d = {"a": 3, "b": 2}
update_counts("aaab", counts_d)
assert counts_d["a"] == 6
assert counts_d["b"] == 3