import simplegui

# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!", [120, 100], 24, "White")
    canvas.draw_circle([100, 100], 2, 2, "Red")

# create frame
frame = simplegui.create_frame("Test", 300, 200)

# register draw handler
frame.set_draw_handler(draw)

# start frame
frame.start()