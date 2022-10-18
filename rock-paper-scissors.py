"""
rock-paper-scissors.py
Arianna Bikombe
October 16, 2022

RPS-7 (Rock, Paper, Scissors, Sponge, Fire, Water and Air)

Prompts the user for an item, and compares it to the computer's randomly-generated response against a set of game rules. Once the user enters their desired item, the LED that corresponds with that item will turn on for 1 second then off again:

	1. Red - Fire
	2. Orange - Rock
	3. Yellow - Sponge
	4. Green - Air
	5. Blue - Water
	6. Purple - Scissors
	7. Pink - Paper

Then, once the computer chooses its item the LED corresponding with that item will turn on for the same amount of time. Finally, whichever item wins between the two will blink five times at a 0.5-second interval, indicating the winner.
"""
# __doc__ attribute used for documentation - learned from COMP525
#!/usr/bin/env python
# import RPi.GPIO as GPIO
# import time
import random    # For use in get_computer_response()

# LED Variables

# LedPinRedFire = 20    # pin GPIO20
# LedPinOrangeRock = 21    # pin GPIO21
# LedPinYellowSponge = 22    # pin GPIO22
# LedPinGreenAir = 23    # pin GPIO23
# LedPinBlueWater = 24    # pin GPIO24
# LedPinPurpleScissors = 25    # pin GPIO25
# LedPinPinkPaper = 26    # pin GPIO26

# LED Setup

# GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by standard marking

# GPIO.setup(LedPinRedFire, GPIO.OUT)   # Set mode to output
# GPIO.output(LedPinRedFire, GPIO.HIGH) # Set high(+3.3V) to turn off led

# GPIO.setup(LedPinOrangeRock, GPIO.OUT)   # Set mode to output
# GPIO.output(LedPinOrangeRock, GPIO.HIGH) # Set high(+3.3V) to turn off led

# GPIO.setup(LedPinYellowSponge, GPIO.OUT)   # Set mode to output
# GPIO.output(LedPinYellowSponge, GPIO.HIGH) # Set high(+3.3V) to turn off led

# GPIO.setup(LedPinGreenAir, GPIO.OUT)   # Set mode to output
# GPIO.output(LedPinGreenAir, GPIO.HIGH) # Set high(+3.3V) to turn off led

# GPIO.setup(LedPinBlueWater, GPIO.OUT)   # Set mode to output
# GPIO.output(LedPinBlueWater, GPIO.HIGH) # Set high(+3.3V) to turn off led

# GPIO.setup(LedPinPurpleScissors, GPIO.OUT)   # Set mode to output
# GPIO.output(LedPinPurpleScissors, GPIO.HIGH) # Set high(+3.3V) to turn off led

# GPIO.setup(LedPinPinkPaper, GPIO.OUT)   # Set mode to output
# GPIO.output(LedPinPinkPaper, GPIO.HIGH) # Set high(+3.3V) to turn off led

# LED Blink Functions

# def led_blink_strong(led_to_blink):
	# GPIO.output(led_to_blink, GPIO.LOW)    # LED on
    # time.sleep(1)    # On for 1 second
	# GPIO.output(led_to_blink, GPIO.LOW)    # LED off
	# time.sleep(0.5)    # Off for 0.5 seconds

# def led_blink_rapid(led_to_blink):
	# for blink_num in range(1, 5)    # Blink 5 times
		# GPIO.output(led_to_blink, GPIO.LOW)  # LED on
		# time.sleep(0.5)    # On for 0.5 seconds
		# GPIO.output(led_to_blink, GPIO.LOW)  # LED off
		# time.sleep(0.5)    # Off for 0.5 seconds

# Response: [Items that any given response defeats]
game_rules = {
	'Rock': ['pounds out Fire', 'crushes Scissors', 'crushes Sponge'],
	'Paper': ['fans Air', 'covers Rock', 'floats on Water'],
	'Scissors': ['swish through Air', 'cut Paper', 'cut Sponge'],
	'Fire': ['melts Scissors', 'burns Paper', 'burns Sponge'],
	'Sponge': ['soaks Paper', 'uses Air pockets', 'absorbs Water'],
	'Air': ['blows out Fire', 'erodes Rock', 'evaporates Water'],
	'Water': ['erodes Rock', 'puts out Fire', 'rusts Scissors']
}

def user_input():
	"""
	Prompts user for item, and sets unvalidated_user_response to their response and calls get_user_response() for validation

		Parameters:
			None

		Returns:
			None
	"""
	# Prompt user for item
	unvalidated_user_response = input("Rock, Paper, Scissors, Fire, Sponge, Air, Water? ")
	get_user_response(unvalidated_user_response)

def get_user_response(user_response):
	"""
	Validates user_input() value, and calls result() function with the user response as its parameter

		Parameters:
			user_response (str): User's response

		Returns:
			None
	"""
	# Matches title-cased user response to one of the items
	# If user's input does not match any item, prompt user again
	match user_response.title():
		case 'Rock':
			# led_blink_strong(LedPinOrangeRock)
			result('Rock')
		case 'Paper':
			# led_blink_strong(LedPinPinkPaper)
			result('Paper')
		case 'Scissors':
			# led_blink_strong(LedPinPurpleScissors)
			result('Scissors')
		case 'Fire':
			# led_blink_strong(LedPinRedFire)
			result('Fire')
		case 'Sponge':
			# led_blink_strong(LedPinYellowSponge)
			result('Sponge')
		case 'Air':
			# led_blink_strong(LedPinGreenAir)
			result('Air')
		case 'Water':
			# led_blink_strong(LedPinBlueWater)
			result('Water')
		case _:
			print('Invalid Response. Please Try Again.')
			user_input()

def get_computer_response():
	"""
	Sets computer_response to an item based on a randomly-generated number

		Parameters:
			None

		Returns:
			computer_reponse (str): Computer's response
	"""
	# Randomly generate number between 1 and 7, including 1 and 7
	computer_number = random.randint(1,7)
	computer_reponse = 'No Response Yet'

	# Matches generated number to one of the items
	match computer_number:
		case 1:
			# led_blink_strong(LedPinOrangeRock)
			computer_reponse = 'Rock'
		case 2:
			# led_blink_strong(LedPinPinkPaper)
			computer_reponse = 'Paper'
		case 3:
			# led_blink_strong(LedPinPurpleScissors)
			computer_reponse = 'Scissors'
		case 4:
			# led_blink_strong(LedPinRedFire)
			computer_reponse = 'Fire'
		case 5:
			# led_blink_strong(LedPinYellowSponge)
			computer_reponse = 'Sponge'
		case 6:
			# led_blink_strong(LedPinGreenAir)
			computer_reponse = 'Air'
		case 7:
			# led_blink_strong(LedPinBlueWater)
			computer_reponse = 'Water'
		case _:
			print('Invalid Computer Response')
	
	# Print and return computer's response
	print('I entered', computer_reponse)
	return computer_reponse

def check_tie(user_response, computer_response):
	"""
	Checks for a tie between the user's response and the computer's response

		Parameters:
			user_response (str): User's response
			computer_response (str): Computer's response

		Returns:
			True/False (bool): Whether user_response and computer_response are equal
	"""
	# If user's response and computer's response are equal,
	# prompt user to try again
	if user_response == computer_response:
		print('Tie. Try Again.')
		return True
	else:
		return False

def match_to_rules(game_rules, your_item, computer_item):
	"""
	Loops through game rules to find user's response, then loops through items

		Parameters:
			game_rules (dict): Game items and the items that they defeat
			your_item (str): User's response
			computer_item (str): Computer's response

		Returns:
			None
	"""
	# Loop through game rules to find your item
	for your_item_key in game_rules.keys():
		# Once you find your item, loop through items that your item defeats
		if your_item == your_item_key:
			for computer_item_value in game_rules.get(your_item_key):
				# If the computer's item is under the list, print out that you defeat the computer
				if computer_item in computer_item_value:
					print(your_item, computer_item_value, '. You win.')
					# Blink winning LED
					# match your_item:
						# case 'Rock':
							# led_blink_rapid(LedPinOrangeRock)
						# case 'Paper':
							# led_blink_rapid(LedPinPinkPaper)
						# case 'Scissors':
							# led_blink_rapid(LedPinPurpleScissors)
						# case 'Fire':
							# led_blink_rapid(LedPinRedFire)
						# case 'Sponge':
							# led_blink_rapid(LedPinYellowSponge)
						# case 'Air':
							# led_blink_rapid(LedPinGreenAir)
						# case 'Water':
							# led_blink_rapid(LedPinBlueWater)
						# case _:
							# print('Invalid')

	# If the computer's item is not under the list of items that your item defeats,
	# loop through game rules to find the computer's item
	for computer_item_key in game_rules.keys():
		# Once you find computer's item, loop through items that your computer's item defeats
		if computer_item == computer_item_key:
			for your_item_value in game_rules.get(computer_item_key):
				# If your item is under the list, print out that it defeats you
				if your_item in your_item_value:
					print(computer_item, your_item_value, '. I win!')
					# Blink winning LED
					# match computer_item:
						# case 'Rock':
							# led_blink_rapid(LedPinOrangeRock)
						# case 'Paper':
							# led_blink_rapid(LedPinPinkPaper)
						# case 'Scissors':
							# led_blink_rapid(LedPinPurpleScissors)
						# case 'Fire':
							# led_blink_rapid(LedPinRedFire)
						# case 'Sponge':
							# led_blink_rapid(LedPinYellowSponge)
						# case 'Air':
							# led_blink_rapid(LedPinGreenAir)
						# case 'Water':
							# led_blink_rapid(LedPinBlueWater)
						# case _:
							# print('Invalid')

def play_again():
	"""
	Ask user if they want to play again, start game over if 'Y', end game if 'N'

		Parameters:
			None

		Returns:
			None
	"""
	play_again = input('Play again? Y/N: ')

	# Variables for counting invalid tries
	try_num = 1
	num_of_more_tries = 9
	
	# If 'Y', start game over
	# If 'N', end game
	# If any other input, give user num_of_more_tries more tries to answer 'Y' or 'N'
	if play_again.title() == 'Y':
		user_input()
	elif play_again.title() == 'N':
		print('Thank you for playing!')
	else:
		while try_num <= num_of_more_tries:
			input('Invalid. Play again? Y/N: ')
			try_num += 1
		print('Maximum of', num_of_more_tries + 1, 'tries exceeded. Goodbye.')
		
def result(user_response):
	"""
	Gets validated user input from from get_user_response(), and calls remaining functions in sequential order for gameplay

		Parameters:
			user_response (str): User's response

		Returns:
			None
	"""
	# Print out user's response
	print('You entered', user_response)

	# Get computer's randomized response
	computer_response = get_computer_response()

	# If there is a tie, start game over
	# Otherwise, continue with gameplay and match responses to the rules
	if check_tie(user_response, computer_response) == True:
		user_input()
	else:
		match_to_rules(game_rules, user_response, computer_response)
	
	# Ask to play again
	play_again()

def main():
	"""
    Main starting point for the program
    """
	user_input()

# Sets main() function as starting point - learned in COMP525
if __name__ == "__main__":
    main()
