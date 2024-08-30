fname = input("enter file name: ")
fhandle = open(fname)

counter = 0
total = 0

for line in fhandle:
    if line.startswith("X-DSPAM-Confidence"):
        counter = counter + 1
        position = line.find(" ")
        str_num = line[position:]
        str_num = str_num.strip()
        flt_num = float(str_num)
        total = total + flt_num

print("Average spam confidence:", total / counter)