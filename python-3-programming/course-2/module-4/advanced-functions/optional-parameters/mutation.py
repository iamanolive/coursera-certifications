def f1(a, L = []):
    L.append(a)
    return L

print(f1(1))
print(f1(2))
print(f1(3))
print(f1(4, ["Hello"]))
print(f1(5, ["Hello"]))