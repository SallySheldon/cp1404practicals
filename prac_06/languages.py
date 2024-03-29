"""
CP1404 Practical 06 - Intermediate exercises
Estimated time to complete Exercise: 30 mins
Actual time to complete: 40 mins (including thinking, etc)

Client code for program to use ProgrammingLanguage class
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Code to create and display programming language objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
