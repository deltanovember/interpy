# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

import simplegui
import random
import math

num_range = 100
num_guesses = 0

def get_num_guesses(range):
    if (range == 100):
        return 7
    else:
        return 10

def get_secret_number():
    return random.randint(0, num_range)

secret_number = get_secret_number()

def begin_game(range):
    global num_range, num_guesses, secret_number
    num_range = range
    num_guesses = get_num_guesses(range)    
    secret_number = random.randint(0, num_range)
    print "New game. Range is from 0 to " + str(num_range)
    print "Number of remaining guesses is " + str(num_guesses) + "\n"

def get_input(text):
    user_guess = int(text)
    global num_guesses, secret_number
    num_guesses = num_guesses - 1
    print "Guess was " + text
    print "Number of remaining guesses is " + str(num_guesses)
    if (num_guesses == 0 and (secret_number != user_guess)):
        print "You ran of guesses. The number was " + str(secret_number) + "\n"
        begin_game(num_range)
    elif (secret_number > user_guess):
        print "Higher!\n"
    elif (secret_number < user_guess):
        print "Lower!\n"
    else:	
        print "Correct!\n"
        begin_game(num_range)
    

def range100():
    global num_range, num_guesses, secret_number
    num_range = 100
    begin_game(num_range)

def range1000():
    global num_range, num_guesses, secret_number
    num_range = 1000
    num_guesses = 10
    secret_number = random.randint(0, num_range)
    begin_game(num_range)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Guess", 200, 200)
frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)


# Start the frame animation
frame.start()
range100()
