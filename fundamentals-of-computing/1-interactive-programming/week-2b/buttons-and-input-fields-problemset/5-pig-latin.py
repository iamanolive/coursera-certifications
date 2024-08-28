import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    if first_letter != "a" and first_letter != "e" and first_letter != "i" and first_letter != "o" and first_letter != "u":
        return rest_of_word + first_letter + "ay"
    else:
        return word + "way"
# Handler for input field

def get_input(input):
    print pig_latin(input)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("Word", get_input, 100)

# Start the frame animation
frame.start()