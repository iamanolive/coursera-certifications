scores = [
    ("rodney dangerfield", -1),
    ("marlon brando", 1),
    ("you", 100)
]

for person in scores:
    name = person[0]
    score = person[1]
    print("hello {}. Your score is {}.".format(name, score))




original_price = float(input("enter original price: "))
discount = float(input("enter discount percentage: "))
new_price = (1 - discount / 100) * original_price
calculation = "${:.2f} discounted by {}% is ${:.2f}".format(original_price, discount, new_price)
print(calculation)