#! /usr/bin/env python
# "This is a dice simulation program. Written by Frank Huang."

import random
import specialInput

number = specialInput.int_inputdice("How many dice would you like to roll?")
side = specialInput.int_inputside("How many sides on your dice?")

for i in range(1, number+1): 
	answer = random.randint(1,side)
	print("Dice {} shows: {}".format(i, answer))