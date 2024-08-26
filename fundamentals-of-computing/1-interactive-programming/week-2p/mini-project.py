import simplegui
import random

# start and restart game

secret_number = 0
remaining_guesses = 7
current_range = 100

def new_game():
    global secret_number, current_range
    secret_number = random.randrange(0, current_range)
    print "New Game!"
    if current_range == 100:
        print "Range is from 0 to 100"
    else:
        print "Range is from 0 to 1000"
    

def range100():
    global remaining_guesses, current_range
    remaining_guesses = 7
    current_range = 100
    new_game()

def range1000():
    global remaining_guesses, current_range
    remaining_guesses = 10
    current_range = 1000
    new_game()

# main game logic
def input_guess(guess):
    global remaining_guesses
    guess = int(guess)
    print "Guess was", guess
    if guess < secret_number:
        print "Higher"
        remaining_guesses = remaining_guesses - 1
        print "You have", remaining_guesses, "guesses left."
    elif guess > secret_number:
        print "Lower"
        remaining_guesses = remaining_guesses - 1
        print "You have", remaining_guesses, "guesses left."
    else:
        print "Correct"
        new_game()
    if remaining_guesses == 0:
        print "Sorry, you lost"
        new_game()

# create frame
frame = simplegui.create_frame("Guess the Number", 300, 300)

# register event handlers
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Guess", input_guess, 190)

# call new game
new_game()