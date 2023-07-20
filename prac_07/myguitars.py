"""
CP1404 Practical 07 - Intermediate Exercises
More Guitars!

Estimated working time for this exercise: 40 minutes
Actual working time: 25 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Read a file of guitar details, prompt user to enter new guitar details, store details in a list of Guitar
    objects, and display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    # File format is like: Model,Year,Price
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # Construct a Guitar object using the elements
        # year should be an int, price should be a float
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the Guitar object to the list
        guitars.append(guitar)
    in_file.close()
    guitars.sort()  # Sort guitars by year (oldest to newest)

    # Loop through and display all guitars (using their str method)
    print("These are your current guitars:")
    for guitar in guitars:
        print(guitar)

    # Prompt user to enter details of new guitars
    print("\nEnter your new guitars (or type Enter to quit):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("Name: ")

    # Save updated guitar details to file
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(guitar.name, guitar.year, guitar.cost, sep=',', file=out_file)
    out_file.close()


main()
