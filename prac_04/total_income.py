"""
CP1404 Practical 05 - Lists, Strings
Starter code for cumulative total income program
Modified for practical exercise
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """Print a report of monthly and cumulative income from a supplied list of monthly incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print(f"Month {(month + 1):2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
