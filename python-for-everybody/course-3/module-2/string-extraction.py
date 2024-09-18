import re

x = "From stephen.marquard@utc.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall('\S+@\S+', x)
print(y) # ["stephen.marquard@utc.ac.za"]
y = re.findall('^From (\S+@\S+)', x)
print(y) # ["stephen.marquard@utc.ac.za"]



data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@"); print(atpos)
sppos = data.find(" ", atpos); print(sppos)
host = data[atpos + 1 : sppos]; print(host)

words = data.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])

y = re.findall('@([^ ]*)', data)
print(y) # ["utc.ac.za"]

y = re.findall('^From .*@([^ ]*)', data)
print(y) # ["utc.ac.za"]