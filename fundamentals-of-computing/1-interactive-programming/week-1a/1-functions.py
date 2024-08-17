# functions

# computes the area of a triangle
def triangle_area(base, height):
    area = 0.5 * base * height
    return area

a1 = triangle_area(3, 8); print a1
a2 = triangle_area(14, 2); print a2

# converts fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5.0 / 9.0) * (fahrenheit - 32)
    return celsius

c1 = fahrenheit_to_celsius(32)
c2 = fahrenheit_to_celsius(212)
print c1, c2

# converts fahrenheit to kelvin
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

k1 = fahrenheit_to_kelvin(32)
k2 = fahrenheit_to_kelvin(212)
print k1, k2

# prints hello world
def hello():
    print "hello world!"

hello()
h = hello()
print h