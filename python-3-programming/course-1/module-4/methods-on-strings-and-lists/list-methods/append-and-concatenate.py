# append method
original_list = [45, 32, 88]
original_list.append("cat")

# concatenation
original_list = [45, 32, 88]
original_list = original_list + ["cat"]



original_list = [45, 32, 88]
print("original list:", original_list)
print("identifier:", id(original_list))

new_list = original_list + ["cat"]
print("new list:", new_list)
print("identifier:", id(new_list))

original_list.append("cat")
print("original list:", original_list)
print("identifier:", id(original_list))



original_list = [45, 32, 88]
alias_list = original_list
original_list = original_list + ["cat"]
print(original_list, alias_list)

original_list = [45, 32, 88]
alias_list = original_list
original_list += ["cat"]
print(original_list, alias_list)