# globals (state)
# helper functions
# classes
# define event handlers
# create frame
# register event handlers
# start frame and timers


import simplegui

# global variables
counter = 0

# helper functions
def increment():
    global counter
    counter = counter + 1

# define event handlers
def tick():
    increment()
    print counter
def buttonpress():
    global counter
    counter = 0

# create frame
frame = simplegui.create_frame("SimpleGUI Test", 100, 100)

# register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("click me!", buttonpress)

# start frame and timers
frame.start()
timer.start()