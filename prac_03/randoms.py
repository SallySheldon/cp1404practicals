"""
CP1404 - Prac 03 - Walkthrough examples
Random Numbers
"""

# SUPPLIED EXAMPLES:
# import random

# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# The function returned random integers between 5 and 20 inclusive.
# The smallest number that can be returned is 5 and the largest 20.
# This is because the function returns a random integer in the range [5, 20]
# inclusive of both end points (5 and 20).

# What did you see on line 2?
# The function returned random numbers from the series 3, 5, 7, 9.
# That's because this function returns a random item from the range 3
# (inclusive) upwards to but exclusive of 10, using steps (increments) of 2 -
# i.e. a number (integer) from the series 3, 5, 7, 9.
# The smallest number that could be returned is 3 and the largest 9.
# It cannot return a 4 as it can only return odd numbers (steps of 2 from 3).

# what did you see on line 3?
# The function returned random real floating-point numbers between 2.5 and 5.5.
# The smallest number that can be returned is 2.5 (as a floating-point number)
# and the largest 5.5 (depending on rounding).


# CODE EXERCISE:
# Produce a random number between 1 and 100 inclusive.
import random

print(random.uniform(1, 100))  # produces a floating-point number
print(random.randint(1, 100))  # produces an integer
