"""
CP1404 Practical 06 - Intermediate exercises
Construct program to use ProgrammingLanguage class
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Code to create and display programming language objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)


main()
