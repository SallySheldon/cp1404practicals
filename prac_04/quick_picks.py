"""
CP1404 - Practical 05 - Do-from-scratch Exercises
'Quick Pick' Lottery Ticket Generator
"""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_QUICK_PICK = 6


def main():
    """Program to generate and display a user-inputted number of 6-number quick pick draws."""
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_QUICK_PICK):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        for number in quick_pick:
            print(f"{number:2} ", end="")
        print()


main()
