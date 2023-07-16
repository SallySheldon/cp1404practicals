"""
CP1404 Practical 06 - Do-from-scratch Exercises - Guitars!
Define a Guitar class
Estimated time to complete: 10 mins
Actual time to complete: 10 mins
"""


class Guitar:
    """Represent details about a guitar in a Guitar object.

    name: string, name of guitar object
    year: integer, year of manufacture
    cost: float, cost in dollars and cents
    """

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, year):
        """Return the age in years of a Guitar object using current year."""
        age = year - self.year
        return age

    def is_vintage(self, year):
        """Determine whether a Guitar object is 50 or more years old (vintage)."""
        age = self.get_age(year)
        return age >= 50
