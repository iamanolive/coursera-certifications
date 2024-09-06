fname = input("enter file name: ")
fhandle = open(fname)

wordlist = list()

for line in fhandle:
    words = line.split()
    for word in words:
        word = word.strip()
        if word not in wordlist:
            wordlist.append(word)

wordlist.sort()
print(wordlist)