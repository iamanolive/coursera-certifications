import simplegui
import random

# global variables
message = "Python is fun!"
position = [50, 50]
width = 500
height = 500
interval = 2000

# text box handler
def update(text):
    global message
    message = text
    
# timer handler
def tick():
    global position # optional
    # changing elements of variable
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y
    
# draw handler
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")
    
# create frame
frame = simplegui.create_frame("Home", width, height)

# register event handlers
text = frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame animation
frame.start()
timer.start()