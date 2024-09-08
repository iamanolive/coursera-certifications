import turtle

# setting up the turtle
wn = turtle.Screen()
alex = turtle.Turtle()

# creating a square
for i in [0, 1, 2, 3]:
    alex.forward(50)
    alex.left(90)

# changing pen color
for aColor in ["yellow", "red", "purple", "blue"]:
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()