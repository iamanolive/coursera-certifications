olympians = [
    ("John Aalberg", 31, "Cross Country Skiing"),
    ("Minna Maarit Aalto", 30, "Sailing"),
    ("Win Valdemar Aaltonen", 54, "Art Competitions"),
    ("Wakako Abe", 18, "Cycling")
]

output_file = open("reduced_olympics.csv", "w")

header_row = "Name,Age,Sport"
output_file.write(header_row + "\n")

for olympian in olympians:
    row_string = ",".join([str(olympian[0]), str(olympian[1]), str(olympian[2])])
    row_string = str(olympian[0]) + "," + str(olympian[1]) + "," + str(olympian[2])
    row_string = "{},{},{}".format(olympian[0], olympian[1], olympian[2])
    output_file.write(row_string + "\n")

output_file.close()