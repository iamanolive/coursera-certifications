import simplegui 

message = "My second frame!"

# Handler for mouse click
def click():
    print message

# Assign callbacks to event handlers
frame = simplegui.create_frame("My second frame", 200, 100)
frame.add_button("Click me", click)

# Start the frame animation
frame.start()