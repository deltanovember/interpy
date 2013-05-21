# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = [HALF_PAD_WIDTH, (HEIGHT - PAD_HEIGHT) / 2]
paddle2_pos = [WIDTH - PAD_WIDTH + HALF_PAD_WIDTH, (HEIGHT - PAD_HEIGHT) / 2]
ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
vel = [0, 1]
p1_score = 0
p2_score = 0

def reset():
    global p1_score, p2_score
    p1_score = 0
    p2_score = 0
    left = random.randrange(2) == 0
    ball_init(left)
    
# pos - top left
def draw_paddle(c, pos):
    color = "White"
    #pos[0] += PAD_WIDTH/2
    top_right = [pos[0] + PAD_WIDTH, pos[1]]
    bottom_left = [pos[0], pos[1] + PAD_HEIGHT]
    bottom_right = [pos[0] + PAD_WIDTH, pos[1] + PAD_HEIGHT]
    #c.draw_line(pos, top_right, 10, color)
    
    c.draw_line(pos, bottom_left, 8, color) 
    #c.draw_line(bottom_right, top_right, 2, color) 
    #c.draw_line(bottom_left, bottom_right, 2, color) 
    
# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    vel[0] = -random.randrange(6, 12)
    vel[1] = -random.randrange(3, 6)
    if right:
        vel[0] = -vel[0]  
    


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    left = random.randrange(2) == 0
    ball_init(left)

def draw(c):
    global p1_score, p2_score, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    p1y = paddle1_pos[1] + paddle1_vel[1]
    p2y = paddle2_pos[1] + paddle2_vel[1]
    if p1y >= 0 and (p1y + PAD_HEIGHT) <= HEIGHT:    
        paddle1_pos[1] += paddle1_vel[1]
    if p2y >= 0 and (p2y + PAD_HEIGHT) <= HEIGHT:
        paddle2_pos[1] += paddle2_vel[1]
    
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    draw_paddle(c, paddle1_pos)
    draw_paddle(c, paddle2_pos)
     
    # update ball
    ball_pos[0] = ball_pos[0] + vel[0]
    ball_pos[1] = ball_pos[1] + vel[1]
    
    # Never cross
    #if ball_pos[0] + BALL_RADIUS > WIDTH - PAD_WIDTH:
    #    ball_pos[1] = WIDTH - PAD_WIDTH - BALL_RADIUS
    
    # check top/bottom collisions
    if ball_pos[1] == BALL_RADIUS or ball_pos[1] == HEIGHT - BALL_RADIUS:
        vel[1] = -vel[1]
        
    def within_paddle(paddle_pos, paddle_height, ball_y):
        return ball_y > paddle_pos[1] and ball_y < paddle_pos[1] + paddle_height
    # check gutter collisions
    accel = 1.1
    if ball_pos[0] <= PAD_WIDTH or ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        # paddle collisions
        if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH and within_paddle(paddle2_pos, PAD_HEIGHT, ball_pos[1]):
            vel[1] = -vel[1] * accel
            vel[0] = -vel[0] * accel
        else:
            if ball_pos[0] <= PAD_WIDTH:
                p2_score += 1
            if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
                p1_score += 1
            right = vel[0] < 0
            ball_init(right)
            
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    c.draw_text(str(p1_score), (140, 50), 50, "White")
    c.draw_text(str(p2_score), (440, 50), 50, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 10
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = vel        
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = vel 
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset, 200)


# start frame
frame.start()
new_game()
