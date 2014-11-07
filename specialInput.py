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

def int_input(prompt):
	"""
		Allows the user to input an integer, and asks for another try if none integer id entered.
	"""
	while True:
		answer = raw_input(prompt)
		try:
			answer = int(answer)
			if answer < 4:
				print("Your dice should have more than 2 faces.")
			else:
				break
		except ValueError:
			print("The sides you enter is not a interger.")
	
	return answer
			

def float_input(prompt):
	while True:
		answer = raw_input(prompt)
		try:
			answer = float(answer)
			return answer
		except ValueError:
			print("That's isn't a real number, please try again.")

def truncate(number, digits):
	number = number * (10 ** digits)
	number = math.floor(number)
	number = number / (10 ** digits)
	return number