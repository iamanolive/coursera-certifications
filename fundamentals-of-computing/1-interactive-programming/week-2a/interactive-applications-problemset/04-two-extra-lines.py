import simplegui

message = "My first frame!"

# Handler for mouse click
def click():
    global message
    print message

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)

frame.start()