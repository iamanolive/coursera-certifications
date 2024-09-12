inventory = {
    "apples": 430,
    "bananas": 312,
    "oranges": 525,
    "pears": 217
}

del inventory["pears"] # delete
inventory["apples"] = 0 # update

inventory["bananas"] = inventory["bananas"] + 200
num_items = len(inventory)

