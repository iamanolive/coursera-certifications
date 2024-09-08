a = "i have had an apple on my desk before!"

# count() is case sensitive
print(a.count("e"))
print(a.count("ha"))

z = ["atoms", 4, "neutron", 6, "proton", 4, "electron", 4, "electron", "atoms"]

print(z.count("4")) # 0
print(z.count(4)) # 3
print(z.count("a")) # 0 
print(z.count("electron")) # 2