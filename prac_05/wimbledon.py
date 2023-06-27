"""
CP1404 Practical 05
Do-from-scratch Exercises
Game, Set, Match
Estimate:   30 minutes
Actual:     65 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Program to read from data file and display the names of the men's Wimbledon singles champions, how many times
    they have won, and their countries."""
    results = process_file(FILENAME)
    champion_to_wins = store_champion_wins(results)
    countries = store_countries(results)
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(champion, wins)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(', '.join(sorted(countries)))


def process_file(filename):
    """Extract annual Wimbledon champion and nationality details from a supplied file and return them as a nested
    list."""
    results = []
    with open(filename, 'r', encoding='utf-8-sig') as in_file:
        in_file.readline()  # Ignore header row
        # Extract year, nationality, champion for each annual result
        for line in in_file:
            result = line.strip().split(',')[:(INDEX_CHAMPION + 1)]
            results.append(result)
    return results


def store_champion_wins(results):
    """Store the number of wins per champion in a dictionary."""
    champion_to_wins = {}
    for result in results:
        try:
            champion_to_wins[result[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_wins[result[INDEX_CHAMPION]] = 1
    return champion_to_wins


def store_countries(results):
    """Store the countries of the champions in a set."""
    countries = {result[INDEX_COUNTRY] for result in results}
    return countries


main()
