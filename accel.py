import simplegui

WIDTH = 600
HEIGHT = 600
BALL_RADIUS = 2
t = 0
a = 0
ball_pos = [10, 20]
vel = [0, 0]
# Handler to draw on canvas
def draw(canvas):
    global t, a
    t+=1
    a+= 0.00001
    vel[0] = vel[0] + t*a
    vel[1] = vel[1] + t*a
    
    canvas.draw_line((50, 50), (180, 50), 2, "Blue")
    canvas.draw_line((180, 140), (180, 50), 2, "Blue")    
    canvas.draw_line((180,140), (50,140), 2, "Blue")
    canvas.draw_line((50, 50), (50,140), 2, "Blue")
    ball_pos[0] += t*vel[0]
    ball_pos[1] += t*vel[1]
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")    
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
# Start the frame animation
frame.set_draw_handler(draw)

frame.start()
