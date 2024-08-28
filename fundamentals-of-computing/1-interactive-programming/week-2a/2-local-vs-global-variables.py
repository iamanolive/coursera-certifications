# global variable
num1 = 1
print num1

def fun():
    # creation of local copy
    num1 = 2
    # local variable
    num2 = num1 + 1
    print num2
    
fun()

print num1
# num2 cannot be called outside fun


def fahrenheit_to_kelvin(fahrenheit):
    celsius = 5.0 / 9.0 * (fahrenheit - 32)
    zero_celsius_in_kelvin = 273.15
    kelvin = celsius + zero_celsius_in_kelvin
    return kelvin

print fahrenheit_to_kelvin(32)
print fahrenheit_to_kelvin(212)


num = 4

def fun1():
    global num
    num = 5

def fun2():
    global num
    num = 6    
    
print num
fun1()
print num
fun2()
print num