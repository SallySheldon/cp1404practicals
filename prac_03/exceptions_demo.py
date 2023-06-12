"""
CP1404 - Practical 03
"""

# # Version 1: supplied code
# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")

# Answer the following questions:
# 1. When will a ValueError occur?
# When the user inputs anything other than an integer as
# either the numerator or denominator.

# 2. When will a ZeroDivisionError occur?
# After the user inputs '0' as the denominator (this will be accepted, but
# the program will throw this error when it tries to calculate 'fraction')

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# See below - I have used a while loop to prompt the user to correct any
# attempt to input '0' as the denominator.

# Version 2: avoiding the possibility of a ZeroDivisionError
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
