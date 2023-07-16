"""
CP1404 Practical 06 - Intermediate exercises
Define a class for a programming language
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a programming language object.

        name: string, reference name for object
        typing: string, either Static or Dynamic typing
        reflection:  string, either Yes or No
        year: integer, year language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a programming language object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True/False if programming language object is dynamically typed or not."""
        return self.typing == "Dynamic"
