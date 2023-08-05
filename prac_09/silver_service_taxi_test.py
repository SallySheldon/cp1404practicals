"""
CP1404 Practical 09
Silver Service Taxi derived class test program
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test drive a Silver Service Taxi object to check SilverServiceTaxi class methods."""
    my_fancy_taxi = SilverServiceTaxi(name="Flash 1", fuel=100, fanciness=2)
    my_fancy_taxi.drive(18)
    print(my_fancy_taxi)
    print(f"Current fare is: ${my_fancy_taxi.get_fare():,.2f}")
    my_fancy_taxi.start_fare()
    my_fancy_taxi.drive(100)
    print(my_fancy_taxi)
    print(f"Current fare is: ${my_fancy_taxi.get_fare():,.2f}")


main()
