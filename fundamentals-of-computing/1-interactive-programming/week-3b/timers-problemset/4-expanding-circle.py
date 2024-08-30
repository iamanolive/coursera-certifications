import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1

# timer handler
def tick():
    global radius
    radius += 1
    
# draw handler
def draw(canvas):
    canvas.draw_circle((100, 100), radius, 2, "White")

        
# create frame and timer
frame = simplegui.create_frame("Circle", HEIGHT, WIDTH)
timer = simplegui.create_timer(100, tick)

frame.set_draw_handler(draw)

# start timer
frame.start()
timer.start()