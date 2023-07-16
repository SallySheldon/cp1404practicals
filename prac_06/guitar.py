"""
CP1404 Practical 06 - Do-from-scratch Exercises - Guitars!
Define a Guitar class
Estimated time to complete: 10 mins
Actual time to complete: 10 mins
"""

import datetime  # Use datetime module to obtain the current year

CURRENT_YEAR = datetime.date.today().year
VINTAGE_AGE = 50


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

    def __lt__(self, other):
        """Sort Guitar objects by increasing order of year released."""
        return self.year < other.year

    def get_age(self):
        """Return the age in years of a Guitar object using CURRENT_YEAR."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine whether a Guitar object is vintage (at least VINTAGE_AGE)."""
        age = self.get_age()
        return age >= VINTAGE_AGE
