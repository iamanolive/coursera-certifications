L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0: return x
    else: return -x

L2 = sorted(L1, key = absolute)
print(L2)

L3 = sorted(L1, reverse = True, key = absolute)
print(L3)

L2 = sorted(L1, key = lambda x: absolute(x))
print(L2)