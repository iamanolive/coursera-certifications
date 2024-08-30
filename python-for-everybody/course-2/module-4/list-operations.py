# list concatenation
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)
print(a, b)


# list slicing
t = [9, 41, 12, 3, 74, 15]

print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])


# the append method
stuff = list()

stuff.append("book")
stuff.append(99)
print(stuff)

stuff.append("cookie")
print(stuff)


# the in operator
some = [1, 9, 21, 10, 16]

print(9 in some) # true
print(15 in some) # false
print(20 not in some) # true


# the sort method
friends = ["joseph", "glenn", "sally"]

friends.sort()

print(friends)
print(friends[1])


# built-in functions
nums = [3, 41, 12, 9, 74, 15]

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))