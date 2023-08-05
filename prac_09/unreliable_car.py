"""
CP1404 Practical 09
Unreliable car derived class module
"""

from random import randint

from car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that has a % chance of not driving."""

    def __init__(self, reliability=0.0, **kwargs):
        """Initialise an Unreliable Car object, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability percentage."""
        return f"{super().__str__()}, {self.reliability}% reliable"

    def drive(self, distance):
        """Drive like parent Car after passing a randomised reliability check."""
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
