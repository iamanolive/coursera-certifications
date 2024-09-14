julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(julia[4])


def circle_info(radius):
    """ returns (circumference, area) of
    a circle with radius `radius` """
    circumference = 2 * 3.14159 * radius
    area = 3.14159 * radius * radius
    return (circumference, area)

print(circle_info(10))

def more_circle_info(radius):
    """ returns (circumference, area) of
    a circle with radius `radius` """
    circumference = 2 * 3.14159 * radius
    area = 3.14159 * radius * radius
    return circumference, area

print(circle_info(10))