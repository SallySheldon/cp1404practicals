"""
CP1404 -
Practical 02 - Practice exercises
More scores
"""

from random import randint


def main():
    """Program to generate and evaluate a user-inputted number of random
    scores and output results to file."""
    number_of_scores = get_valid_number()
    out_file = open("results.txt", "w")
    for i in range(number_of_scores):
        score = randint(0, 100)
        result = evaluate_result(score)
        print(f"{score} is {result}", file=out_file)
    out_file.close()


def get_valid_number():
    """Prompt user for a number between 0 and 100."""
    number = int(input("Enter number: "))
    while number < 0 or number > 100:
        print("Number must be between 0 and 100.")
        number = int(input("Enter number: "))
    return number


def evaluate_result(score):
    """Evaluate the result from a given score."""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
