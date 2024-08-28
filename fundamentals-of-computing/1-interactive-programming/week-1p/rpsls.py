import random

def name_to_number(name):
    if name == "rock":
        number = 0
        return number
    elif name == "Spock":
        number = 1
        return number
    elif name == "paper":
        number = 2
        return number
    elif name == "lizard":
        number = 3
        return number
    elif name == "scissors":
        number = 4
        return number
    else:
        error = "Error: name does not match"
        print error

def number_to_name(number):
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "Spock"
        return name
    elif number == 2:
        name = "paper"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "scissors"
        return name
    
def rpsls(player_choice):
    print ""
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    if (player_number - comp_number) % 5 <= 1:
        print "Player wins!"
    elif (player_number - comp_number) % 5 >= 3:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
        
rpsls("scissors")