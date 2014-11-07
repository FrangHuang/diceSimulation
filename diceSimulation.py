#! /usr/bin/env python
# "This is a dice simulation program. Written by Frank Huang."

import random
import specialInput

side = specialInput.int_input("How many sides on your dice?")
answer = random.randint(1,side)
print("The dice shows: " + str(answer))