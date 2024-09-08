# the in operator
print("p" in "apple") # true
print("i" in "apple") # false
print("ap" in "apple") # true
print("pa" in "apple") # false

print("a" in "a") # true
print("apple" in "apple") # true
print("" in "a") # true
print("" in "apple") # true


# the not in operator
print("x" not in "apple") # true


print("a" in [
    "apple", "absolutely",
    "application", "nope"
]) # false

print("a" in [
    "apple", "absolutely",
    "application"
]) # false