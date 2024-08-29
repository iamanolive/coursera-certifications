import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# button handlers
def start():
    timer.start()

def stop():
    timer.stop()

def reset():
    global counter
    counter = 0
        
# create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()