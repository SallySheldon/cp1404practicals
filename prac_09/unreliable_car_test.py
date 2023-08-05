"""
CP1404 Practical 09
Program to test UnreliableCar class.
"""

from unreliable_car import UnreliableCar


def main():
    """Test drive an Unreliable Car object to check UnreliableCar class methods."""
    my_dodgy_car = UnreliableCar(name="Dodge 1", fuel=100, reliability=80)
    print(my_dodgy_car)
    for i in range(0, 10):  # Test drive the car (5km) 10 times
        my_dodgy_car.drive(5)
        print(my_dodgy_car)


main()
