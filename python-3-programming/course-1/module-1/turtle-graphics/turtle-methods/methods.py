import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

distance = 5

tess.up()

for _ in range(30):
    tess.stamp()
    tess.forward(distance)
    tess.right(24)
    distance = distance + 2

wn.exitonclick()