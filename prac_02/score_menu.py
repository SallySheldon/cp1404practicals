"""
CP1404 -
Practical 02 - Do-from-scratch exercises
Menu
"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    """Menu-driven program to evaluate a user-inputted score and print
    that many stars."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = evaluate_result(score)
            print(f"A score of {score} is {result}\n")
        else:
            print_asterisks(score)
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score():
    """Prompt user for a score between 0 and 100."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        score = int(input("Enter score: "))
    return score


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


def print_asterisks(number):
    """Print as many asterisks as a supplied number."""
    print("*" * number)


main()
