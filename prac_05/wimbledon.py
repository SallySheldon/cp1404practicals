"""
CP1404 Practical 05
Do-from-scratch Exercises
Game, Set, Match
Estimate:   30 minutes
Actual:     45 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Program to read file of Wimbledon men's final results and display champions' nationalities and number of wins."""
    filename = FILENAME
    results = process_file(filename)
    champion_to_number = {}
    # Store champion's name (key) and number of times won (value) in dictionary
    for result in results:
        try:
            champion_to_number[result.split(',')[2]] += 1
        except KeyError:
            champion_to_number[result.split(',')[2]] = 1
    print(champion_to_number)
    # Store champions' nationalities in set
    nationalities = {result.split(',')[1] for result in results}
    print(nationalities)


def process_file(filename):
    """Extract annual Wimbledon champion and nationality details from a supplied file and return them as a nested
    list."""
    with open(filename, 'r', encoding='utf-8-sig') as in_file:
        in_file.readline()  # Ignore header row
        results = []
        for line in in_file:
            result = line.strip().split(',')[:3]  # Extract year, country, champion for each annual result
            results.append(result)  # Store annual results in nested list
    return results


main()

