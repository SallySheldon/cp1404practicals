"""
CP1404 Practical 09
Taxi simulator program.
Estimated time to complete: 45 mins
Actual time to complete: 60 mins
"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    """Taxi simulator program."""
    current_taxi = None
    bill_to_date = 0.0
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(TAXIS)
            taxi_choice = get_valid_integer("Choose taxi: ")
            if taxi_choice > len(TAXIS) - 1:
                print("Invalid taxi choice")
            else:
                current_taxi = TAXIS[taxi_choice]
        elif menu_choice == "d":
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
            else:
                distance = get_valid_integer("Drive how far? ")
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:,.2f}")
                bill_to_date += trip_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:,.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill_to_date:,.2f}")
    print("Taxis are now:")
    display_taxis(TAXIS)


def display_taxis(taxis):
    """Display numbered list of available taxis and their current details."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_integer(prompt):
    """Prompt the user for an integer >= 0."""
    is_valid_input = False
    while not is_valid_input:
        try:
            integer = int(input(prompt))
            if integer < 0:
                print("Number must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return integer


main()
