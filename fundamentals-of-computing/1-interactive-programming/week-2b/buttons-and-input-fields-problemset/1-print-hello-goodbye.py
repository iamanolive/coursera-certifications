import simplegui 


# Handlers for buttons
def print_hello():
    print "Hello"
    
def print_goodbye():
    print "Goodbye"

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.add_button("Hello", print_hello)
frame.add_button("Goodbye", print_goodbye)


# Start the frame animation
frame.start()