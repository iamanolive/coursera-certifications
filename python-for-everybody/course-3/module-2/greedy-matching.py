import re

x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y) # ["From: Using the :"]

x = "From: Using the : character"
y = re.findall("^F.+?:", x)
print(y) # ["From:"]