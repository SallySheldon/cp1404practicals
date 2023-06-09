"""
CP1404 -
Practical 02 reworking of Prac 01 program using functions
Fix broken program to determine score status
"""


def main():
    """Program to ask a user for their score and print the evaluated result."""
    score = float(input("Enter score: "))
    result = evaluate_result(score)
    print(result)


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
