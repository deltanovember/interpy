# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

current_key = ' '

def keydown(key):
    global current_key
    current_key = chr(key)
    
def keyup(key):
    global current_key
    current_key = ' '

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(current_key, [10, 25], 20, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
