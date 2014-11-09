"""
	special input module

"""

import math

def name_input(prompt):
		name = raw_input(prompt)
		if len(name) < 11:
			return name
		else:
			print("That's name is too long. I will give you a nick name.")
			name = name[:10]
			return name

def int_inputside(prompt):
	"""
		Allows the user to input an integer, which should be bigger than 3, and asks for another try if none integer is entered.
	"""
	while True:
		answer = raw_input(prompt)
		try:
			answer = int(answer)
			if answer < 2:
				print("Your dice should have more than 1 faces.")
			else:
				break
		except ValueError:
			print("The sides you enter is not an interger.")
	
	return answer

def int_inputdice(prompt):
	"""
		Allows the user to input an integer, which should be bigger than 0, and asks for another try if none integer is entered.
	"""
	while True:
		answer = raw_input(prompt)
		try:
			answer = int(answer)
			if answer < 1:
				print("The number of your dice should bigger than 0.")
			else:
				break
		except ValueError:
			print("The number you enter is not an interger.")
	
	return answer

def float_input(prompt):
	while True:
		answer = raw_input(prompt)
		try:
			answer = float(answer)
			return answer
		except ValueError:
			print("That's isn't a real number, please try again.")
