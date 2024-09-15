def f1(x):
    return x - 1

print(f1(3))
print(f1)
print(type(f1))


lf = lambda x: x - 1
print(lambda x: x - 1)
print(type(lf))
print(lf(3))



def last_char(s):
    return s[-1]

last_char = lambda s: s[-1]
print(last_char("hello"))