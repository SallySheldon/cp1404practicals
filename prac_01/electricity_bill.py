"""
CP1404 Practical 01
Practice work.
Create an electricity bill estimator.
Inputs should be:
price per kWh in cents,
daily use in kWh, and
number of days in the billing period.
"""

print("Electricity bill estimator")
cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
bill = cents_per_kwh * daily_use_kwh * number_of_billing_days / 100  # in dollars
print(f"Estimated bill: ${bill:.2f}")
