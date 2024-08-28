import simplegui 

def draw(canvas):
    canvas.draw_text("This is easy?", [100, 100], 24, "Red")
    

frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)

frame.start()