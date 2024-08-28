import random


def number_to_fortune(number):
    
    if number == 0:
        string = "Yes, for sure!"
        return string
    elif number == 1:
        string = "Probably yes."
        return string
    elif number == 2:
        string = "Seems like yes..."
        return string
    elif number == 3:
        string = "Definitely not!"
        return number
    elif number == 4:
        string = "Probably not."
        return string
    elif number == 5:
        string = "I really doubt it..."
        return string
    elif number == 6:
        string = "Not sure, check back later!"
        return string
    elif number == 7:
        string = "I really can't tell"
        return string
    else:
        print("Error: Invalid Input")

def mystical_octosphere(question):
    print "Your question was...", question
    print "You shake the mystical octosphere."
    answer_number = random.randrange(0, 8)
    answer_fortune = number_to_fortune(answer_number)
    print "The cloudy liquid swirls, and a reply comes into view..."
    print "The mystical octosphere says...", answer_fortune
    print ""
    
    

mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")
