# implementation of card game - Memory

import simplegui
import random
import time

WIDTH = 817

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, 100)
label = frame.add_label("Moves = 0")

# helper function to initialize globals
def init():
    global deck, num_moves, state, exposed, WIDTH, num_moves, last_card, pause_cards, pause_time, num_moves, state  
    deck = range(0,9) + range(0,9)
    exposed = []
    for card in deck:
        exposed.append(False)
    random.shuffle(deck)
    num_moves = 0
    last_card = -1
    pause_cards = []
    pause_time = 0    
    num_moves = 0
    state = 0
    label.set_text("Moves = " + str(num_moves))
    
frame.add_button("Restart", init)   
init()


     
# define event handlers
def mouseclick(pos):
    global num_moves, state, last_card, pause_cards, pause_time
    print 'state' + str(state)
    if 0 == state:
        state = 1
    # add game state logic here
    card = (int) (pos[0]/(WIDTH/16))
    print card
    if not exposed[card]:
        exposed[card] = True
        if 0 == state:
            state = 1
        if 1 == state:
            state = 2
            num_moves+=1
            label.set_text("Moves = " + str(num_moves))
        elif 2 == state:
            state = 1
            if deck[last_card] == deck[card]:
                print 'match'
            elif last_card >= 0:
                exposed[last_card] = False
                exposed[card] = False
                pause_cards = [card, last_card]
                pause_time = time.time()
    
    last_card = card
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global pause_cards
    spacing = 51.4
    offset = 10
    x = offset
    counter = 0
    for num in deck:
        x1 = counter * spacing
        card_width = spacing-7
        if exposed[counter]: 
            canvas.draw_text(str(num), (x, 65), 60, "White")     
        else:
            if counter in pause_cards and time.time() - pause_time < 0.5:
                canvas.draw_text(str(num), (x, 65), 60, "White") 
            else:
                if counter in pause_cards:
                    pause_cards.remove(counter)
                canvas.draw_polygon([(x1, 0), (x1 + card_width, 0), (x1 + card_width, 194), (x1, 194)], 6, "Brown", "Green")
            
        counter+=1
        x += spacing
    pass



# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric