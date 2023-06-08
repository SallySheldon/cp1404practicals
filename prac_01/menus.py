"""
CP1404 Practical 01
Do-from-scratch Exercise 2
Create a simple menu-driven program to say hello and goodbye to the user
"""

MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    choice = input(">>> ").upper()
print("Finished.")
