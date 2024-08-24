# changing the flow of control of the program

def greet(friend, money):
    if friend and (money > 20):
        print "hi!"
        money = money - 20
    elif friend:
        print "hello"
    else:
        print "haha"
        money = money + 10
    return money

money = 15

money = greet(True, money)
print "money:", money
print ""

money = greet(False, money)
print "money:", money
print ""

money = greet(True, money)
print "money:", money
print ""



def is_leap_year(year):
    if (year % 400) == 0: return True
    elif (year % 100) == 0: return False
    elif (year % 4) == 0: return True
    else: return False

year = 2100
leap_year = is_leap_year(year)

if leap_year:
    print year, "is a leap year"
else:
    print year, "is not a leap year"