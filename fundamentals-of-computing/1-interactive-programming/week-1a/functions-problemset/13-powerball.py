def powerball():
    n1 = random.randrange(1, 60)
    n2 = random.randrange(1, 60)
    n3 = random.randrange(1, 60)
    n4 = random.randrange(1, 60)
    n5 = random.randrange(1, 60)
    p_ball = random.randrange(1, 36)
    print "Today's numbers are " + str(n1) + ", " + str(n2) + ", " + str(n3) + ", " + str(n4) + ", and " + str(n5) + ". The Powerball number is " + str(p_ball) + "."


powerball()
powerball()
powerball()