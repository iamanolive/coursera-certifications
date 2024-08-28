import simplegui 

def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    
frame = simplegui.create_frame("It works", 400, 200)
frame.set_draw_handler(draw)
frame.start()