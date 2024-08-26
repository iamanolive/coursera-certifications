import simplegui

# define global value
value = 3.12

# handling single quantities
def convert_units(value, name):
    result = str(value) + " " + name
    if value > 1:
        result = result + "s"
    return result

# converting into dollars and cents
def convert(value):
    # split value into dollars and cents
    dollars = int(value)
    cents = round(100 * (value - dollars))
    # convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")
    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
# define draw handler
def draw(canvas):
    canvas.draw_text(convert(value), [37, 100], 24, "White")

# define input field handler
def input_handler(text):
    global value
    value = float(text)

# create frame
frame = simplegui.create_frame("Converter", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_input("Enter Value", input_handler, 100)

# start frame
frame.start()