import re

x = "we just received $10.00 for cookies"
y = re.findall("\$[0-9.]+", x)
print(y) # ["$10.00"]