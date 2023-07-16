"""
CP1404 Practical 06 - Do-from-scratch Exercises - Guitars!
Program to test that Guitar class methods work as expected.
Estimated time to complete: 15 mins
Actual time to complete: 12 mins
"""

from prac_06.guitar import Guitar

YEAR = 2023


def run_tests():
    """Program to test get_age() and is_vintage() methods in Guitar class definition."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 799.50)
    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age(YEAR)}")
    print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age(YEAR)}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(YEAR)}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(YEAR)}")


run_tests()
