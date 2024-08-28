import simplegui

# defining event handler
def tick():
    print "tick!"
# registering event handler
timer = simplegui.create_timer(1000, tick)
timer.start() # starting timer