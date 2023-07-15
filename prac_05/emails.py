"""
CP1404 Practical 05
Do-from-scratch Exercises
Emails
Estimate:   15 minutes
Actual:     20 minutes
"""


def main():
    """Program to obtain, store and print user-inputted email addresses and corresponding names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract user's name from supplied email address."""
    username = email.split('@')[0]
    name = ' '.join(username.split('.')).title()
    return name


main()
