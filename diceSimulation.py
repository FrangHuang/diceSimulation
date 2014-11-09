#! /usr/bin/env python
# "This is a dice simulation program. Written by Frank Huang."
print("\nThis program simulates rolling several dices.\
\nThe user can choose how many dice are rolled and how many sides on each dice.")

import random
import specialInput

number = specialInput.int_inputdice("\nHow many dice would you like to roll?")

for i in range(1, number+1): 
	side = specialInput.int_inputside("\nHow many sides on dice #{}?".format(i))
	answer = random.randint(1,side)
	print("Dice {} shows: {}".format(i, answer))