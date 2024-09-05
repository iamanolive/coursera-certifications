smallest_so_far = None
print("before", smallest_so_far)

for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None or the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print("after", smallest_so_far)