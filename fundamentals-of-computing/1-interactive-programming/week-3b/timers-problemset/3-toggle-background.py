import simplegui 

color = "Red"

# timer handler
def tick():
    global color
    if color == "Red":
        color = "Blue"
        frame.set_canvas_background(color)
    elif color == "Blue":
        color = "Red"
        frame.set_canvas_background(color)
        
# create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(3000, tick)
frame.set_canvas_background(color)

# start frame and timer
frame.start()
timer.start()