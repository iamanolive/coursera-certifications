inventory = {
    "apples": 430,
    "bananas": 312,
    "oranges": 525,
    "pears": 217
}

# iterating over every key
for key in inventory.keys():
    print(key, "has value", inventory[key])
for k in inventory.keys():
    print("got key", k)


keys = list(inventory.keys())
print(keys)

print(list(inventory.values()))
print(list(inventory.items()))

for key in inventory:
    print(key, "maps to", inventory[key])


print("apples" in inventory)
print("cherries" in inventory)

if "bananas" in inventory:
    print(inventory["bananas"])
else:
    print("we have no bananas")


print(inventory.get("apples"))
print(inventory.get("cherries"))
print(inventory.get("cherries", 0))