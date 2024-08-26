import simplegui

store = 12
operand = 3

def output():
    print "store =", store
    print "operand =", operand
    print ""
    
def swap():
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    global store, operand
    store = store + operand
    output()

def subtract():
    global store, operand
    store = store - operand
    output()
    
frame = simplegui.create_frame("Calculator", 200, 200)

frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Subtract", subtract, 100)

frame.start()