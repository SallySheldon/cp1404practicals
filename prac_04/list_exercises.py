"""
CP1404 - Practical 05 - Lists & Strings
Intermediate Exercises
"""

# Basic list operations
NUMBER_OF_NUMBERS = 5

numbers = []
for i in range(NUMBER_OF_NUMBERS):
    while True:
        try:
            number = int(input("Number: "))
            numbers.append(number)
            break
        except ValueError:
            print("Please enter a valid integer")
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {(sum(numbers) / NUMBER_OF_NUMBERS):.1f}")


# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                        'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                        'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
