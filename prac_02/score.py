"""
CP1404 -
Practical 02 reworking of Prac 01 program using functions
Fix broken program to determine score status
"""

from random import randint


def main():
    """Program to ask a user for their score, generate a random score, and
    print the evaluated results."""
    users_score = float(input("Enter score: "))
    result = evaluate_result(users_score)
    print(f"Your score of {users_score} is {result}")
    random_score = float(randint(0, 100))
    result = evaluate_result(random_score)
    print(f"A random score of {random_score} is {result}")


def evaluate_result(score):
    """Evaluate the result from a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
