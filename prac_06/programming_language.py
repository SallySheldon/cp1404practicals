"""
CP1404 Practical 06 - Intermediate exercises
Define a class for a programming language
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a ProgrammingLanguage object.

        name: string, reference name for object
        typing: string, either Static or Dynamic typing
        reflection:  Boolean, either True or False
        year: integer, year language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine whether a ProgrammingLanguage object is dynamically typed or not."""
        return self.typing == "Dynamic"
