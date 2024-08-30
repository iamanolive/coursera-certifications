# truncates after the decimal
print(3.14, int(3.14))
print(3.999, int(3.999))
print(3.0, int(3.0))
print(-3.999, int(-3.999))


print("2345", int(2345))
print(17, int(17))


print(float("123.45"))
print(type(float("123.45")))


print(str(17))
print(str(123.45))
print(type(str(123.45)))


# application of type conversion
value = 55
print("the value is " + str(value))