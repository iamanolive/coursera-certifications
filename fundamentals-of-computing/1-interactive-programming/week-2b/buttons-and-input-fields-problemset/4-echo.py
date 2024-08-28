import simplegui 

# Handlers for input field

def get_input(input):
    print input
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)
frame.add_input("Echo input", get_input, 100)

# Start the frame animation
frame.start()