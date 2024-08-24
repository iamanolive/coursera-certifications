# comparison operators

a = 7 > 3
print a

x = 5
y = 5
b = x > y
print b

c = "hello" == "hello"
print c
c = "hello" == 'hello'
print c
c = "hello" == "Hello"
print c

d = 20.6 <= 18.3
print d

print (a and b) or (c and (not d))