line = "From stephen.marquard@utc.ac.za Sat Jan  5 09:14:16 2008"
words = line.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])