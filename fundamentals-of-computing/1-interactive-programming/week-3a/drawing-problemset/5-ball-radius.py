import simplegui 

# global variables
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# draw handler
def draw(canvas):
    canvas.draw_circle([150, 150], ball_radius, 2, "White")
    
# event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius += RADIUS_INCREMENT
    
def decrease_radius():
    global ball_radius
    if ball_radius > 5:
        ball_radius -= RADIUS_INCREMENT

# create frame
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)

# assign callbacks to event handlers
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)

# start frame animation
frame.start()