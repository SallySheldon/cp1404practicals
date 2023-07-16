"""
CP1404 Practical 06 - Do-from-scratch Exercises - Guitars!
Program to use Guitar class and methods.
Estimated time to complete: 30 mins
Actual time to complete: 40 mins
"""

from prac_06.guitar import Guitar

YEAR = 2023


def main():
    """Program to store and display details of a user's guitars."""
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))  # Test data
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))  # Test data
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")
    # Calculate alignments for display formatting
    max_number = len(str(len(guitars)))
    max_name = max((len(guitar.name) for guitar in guitars))
    max_cost = max((len(str(guitar.cost)) for guitar in guitars)) + 3  # Add 3 for $ , and . characters

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage(YEAR) else ""
        print(f"Guitar {i:>{max_number}}: {guitar.name:>{max_name}} ({guitar.year}), worth $"
              f"{guitar.cost:>{max_cost},.2f} {vintage_string}")


main()
