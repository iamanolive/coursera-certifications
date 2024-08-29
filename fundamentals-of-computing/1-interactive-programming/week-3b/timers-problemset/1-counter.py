import simplegui 

counter = 0

# timer handler
def tick():
    global counter
    print counter
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)
timer.start()