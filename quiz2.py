# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
	if (name == 'rock'):
		return 0
	elif (name == 'Spock'):
		return 1
	elif (name == 'paper'):
		return 2
	elif (name == 'lizard'):
		return 3		
 	elif (name == 'scissors'):
		return 4
	else:
		print "Invalid name"

def number_to_name(num):
	if (num == 0):
		return 'rock'
	elif (num == 1):
		return 'Spock'
	elif (num == 2):
		return 'paper'
	elif (num == 3):
		return 'lizard'		
 	elif (num == 4):
		return 'scissors'
	else:
		print "Invalid number " + num


def rpsls(name): 
    # convert name to player_number using name_to_number
	player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
	comp_number = random.randrange(0, 4)
    # compute difference of player_number and comp_number modulo five
	difference = (player_number - comp_number) % 5

	# use if/elif/else to determine winner
	winning_message = 'Player and computer tie!'
	if (difference == 1 or difference == 2):
		winning_message = 'Player wins!'
	elif (difference == 3 or difference == 4):
		winning_message = 'Computer wins!'

    # convert comp_number to name using number_to_name
	comp_name = number_to_name(comp_number)

    # print results
	print 'Player choose ' + name
	print 'Computer choose ' + comp_name
	print winning_message + '\n'

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



