"""
CP1404 Practical 09
Program to test Taxi class.
"""

from taxi import Taxi


def main():
    """Test drive a taxi object to check Taxi class methods."""
    my_taxi = Taxi(name="Prius 1", fuel=100)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare is: ${my_taxi.get_fare():,.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare is: ${my_taxi.get_fare():,.2f}")


main()
