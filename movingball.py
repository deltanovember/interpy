import simplegui

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 1]
time = 0

# Handler to draw on canvas
def draw(canvas):
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")


    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
# Start the frame animation
frame.set_draw_handler(draw)

frame.start()
