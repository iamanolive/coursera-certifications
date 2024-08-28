import simplegui 

def draw(canvas):
    canvas.draw_text("X", [0, 35], 48, "White")
    
frame = simplegui.create_frame("X", 96, 96)
frame.set_draw_handler(draw)

frame.start()