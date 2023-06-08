"""
CP1404 Practical 01
Extension work.
Menu-driven number sequence generator:
A school teacher requires a small program that would allow primary school
students to learn about various number sequences. The teacher is interested
in a simple menu-driven program that has the following choices
(where x and y are inputs the user enters once at the start of the program):

Show the even numbers from x to y
Show the odd numbers from x to y
Show the squares from x to y
Exit the program
"""

import math

MENU = """
Generate a sequence of:
(E)ven numbers from x to y
(O)dd numbers from x to y
(S)quare numbers from x to y
OR
(Q)uit the program
"""

print(MENU)
choice = input("Enter choice: ").upper()
while choice != "Q":
    x = int(input("Enter lower (x) value: "))
    y = int(input("Enter upper (y) value: "))
    if choice == "E":
        for i in range(x, y + 1):
            if i != 0 and (i % 2) == 0:
                print(i, end=" ")
    elif choice == "O":
        for i in range(x, y + 1):
            if (i % 2) != 0:
                print(i, end=" ")
    else:
        for i in range(x, y + 1):
            #  Find squares by checking if square root is a whole number
            if i != 0 and int(math.sqrt(i)) == math.sqrt(i):
                print(i, end=" ")
    choice = input("\n\nEnter choice: ").upper()
print("Goodbye.")
