lst = ["leaders", "and", "best"]
string = "/".join(lst)
print(string)

words = ["red", "blue", "green"]
glue = ":"
string = glue.join(words)
print(string, words, sep = "\n")

print("***".join(words))
print("".join(words))