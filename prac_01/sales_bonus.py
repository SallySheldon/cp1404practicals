"""
CP1404 Practical 01
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

HIGH_BONUS_THRESHOLD = 1000
LOW_BONUS_PERCENTAGE = 0.1
HIGH_BONUS_PERCENTAGE = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= HIGH_BONUS_THRESHOLD:
        bonus = sales * HIGH_BONUS_PERCENTAGE
    else:
        bonus = sales * LOW_BONUS_PERCENTAGE
    print(f"Bonus is ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
