music ="pull out your music and dancing can begin"

print(music.index("m")) # 14
print(music.index("your")) # 9

bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(bio.index("Metatarsal")) # 0
print(bio.index([])) # 3
print(bio.index(43)) # 6

# runtime error if item not in sequence