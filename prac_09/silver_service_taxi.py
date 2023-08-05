"""
CP1404 Practical 09
Silver Service Taxi derived class module
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that scales fares by a fanciness factor."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=1.0):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Taxi but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:,.2f}"

    def get_fare(self):
        """Return the price for the Silver Service Taxi trip."""
        return super().get_fare() + self.flagfall
