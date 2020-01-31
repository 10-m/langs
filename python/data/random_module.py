#!env python3
# -*- coding: utf-8 -*-
import random 

numbers = [199, 288, 56, 82, 99, 1, 538, 499]

num_randint  = random.randint(1, 100)
print(num_randint)

num_choice =random.choice(numbers)
print(num_choice)

random.shuffle(numbers)
print(numbers)
