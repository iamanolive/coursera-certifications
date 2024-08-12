my_list = []

word1 = input("first word: ")
word2 = input("second word: ")
word3 = input("third word: ")
word4 = input("fourth word: ")
word5 = input("fifth word: ")

my_list.append(word1)
my_list.append(word2)
my_list.append(word3)
my_list.append(word4)
my_list.append(word5)

my_list.remove(my_list[1])
del my_list[-1]

print(my_list)