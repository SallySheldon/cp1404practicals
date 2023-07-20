"""
CP1404 Practical 01
Do-from-scratch Exercise 1
Shop Calculator program to determine total discounted price
"""

DISCOUNT = 0.1
DISCOUNT_THRESHOLD = 100

total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price
if total > DISCOUNT_THRESHOLD:
    total *= (1 - DISCOUNT)
print(f"Total price for {number_of_items} items is ${total:.2f}")
