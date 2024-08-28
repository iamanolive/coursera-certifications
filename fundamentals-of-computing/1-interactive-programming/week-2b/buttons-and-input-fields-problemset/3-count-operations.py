import simplegui

count = 21

# Define event handlers for four buttons

def reset():
    global count
    count = 0

def increment():
    global count
    count = count + 1

def decrement():
    global count
    count = count - 1

def print_count():
    global count
    print count
    
# Create frame and assign callbacks to event handlers

frame = simplegui.create_frame("Register Buttons", 300, 300)
frame.add_button("Reset", reset, 100)
frame.add_button("Increment", increment, 100)
frame.add_button("Decrement", decrement, 100)
frame.add_button("Print", print_count, 100)

# Start the frame animation

frame.start()