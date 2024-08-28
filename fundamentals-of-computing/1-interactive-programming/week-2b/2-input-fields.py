import simplegui

store = 12
operand = 3

def output():
    """prints contents of store and operand"""
    print "store =", store
    print "operand =", operand
    print ""
    
def swap():
    """swaps content of store and operand"""
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    """adds store and operand and saves value to store"""
    global store, operand
    store = store + operand
    output()

def subtract():
    """subtracts operand from store and saves value to store"""
    global store, operand
    store = store - operand
    output()

def multiply():
    """multiplies store by operand and saves value to store"""
    global store, operand
    store = store * operand
    output()
    
def divide():
    """divides store by operand and saves value to store"""
    global store, operand
    store = store / operand
    output()
    
def enter(input):
    global store, operand
    operand = float(input)
    output()
    
    
frame = simplegui.create_frame("Calculator", 300, 300)

frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Subtract", subtract, 100)
frame.add_button("Multiply", multiply, 100)
frame.add_button("Divide", divide, 100)

frame.add_input("Enter Operand", enter, 100)

frame.start()