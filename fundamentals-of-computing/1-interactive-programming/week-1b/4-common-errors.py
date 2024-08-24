"""

NameError
    misspelled variable or function names
    calling a function from a module without importing the module
    using variables without defining them
    using strings without wrapping them in quotation marks
    
AttributeError
    using the wrong case for call to a function in a module

TypeError
    passing an incorrect number of arguments into a function
    attempted multiplication of string by integer

SyntaxError
    defining function without colon in function header
    using single equal instead of double equal in a conditional statement


"""

# documentation string
import math

def triangle_area(side1, side2, side3):
    """
    returns the area of a triangle
    given the lengths of its three sides
    """
    semi_perimeter = (side1, side2, side3) / 2.0 # heron's formula
    area = math.sqrt(semi_perimeter * 
                     (semi_perimeter - side1) * 
                     (semi_perimeter - side2) * 
                     (semi_perimeter - side3))
    return area