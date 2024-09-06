print(range(4))
friends = ["joseph", "glenn", "sally"]
print(len(friends))
print(list(range(len(friends))))


for friend in friends:
    print("happy new year", friend)

# creating a counted loop
for i in range(len(friends)):
    friend = friends[i]
    print("happy new year", friend)