julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2]) # indexing
print(julia[2:6]) # slicing
print(len(julia)) # length
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)