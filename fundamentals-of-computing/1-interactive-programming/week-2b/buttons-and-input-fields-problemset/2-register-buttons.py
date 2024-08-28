import simplegui 

# Handlers for buttons
def set_red():
    global color
    color = "red"
    
def set_blue():
    global color
    color = "blue"
    
def print_color():
    print color

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)

frame.add_button("Red", set_red)
frame.add_button("Blue", set_blue)
frame.add_button("Print", print_color)


# Start the frame animation
frame.start()