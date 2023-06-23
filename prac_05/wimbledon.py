"""
CP1404 Practical 05
Do-from-scratch Exercises
Game, Set, Match
Estimate:   30 minutes
Actual:     45 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Program to read file of Wimbledon men's final results and report champions' nationality and number of wins."""
    filename = FILENAME
    with open(filename, 'r', encoding='utf-8-sig') as in_file:
        data = in_file.read().split('\n')[1:]  # Split data by year (at \n), removing header row
    champion_to_number = {}
    # Store champion's name (key) and number of times won (value) in dictionary
    for record in data:
        try:
            champion_to_number[record.split(',')[2]] += 1
        except KeyError:
            champion_to_number[record.split(',')[2]] = 1
    print(champion_to_number)
    # Store champions' nationalities in set
    nationalities = {record.split(',')[1] for record in data}
    print(nationalities)


main()

