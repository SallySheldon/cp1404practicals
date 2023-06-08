"""
CP1404 Prac 02
First exercise - Password stars program - Practise committing to Git
"""

DEFAULT_MINIMUM_LENGTH = 8


def main():
    """Program to ask user to set a password meeting minimum length requirements
    then print asterisks as long as the password."""
    minimum_length = DEFAULT_MINIMUM_LENGTH
    password = get_valid_password(minimum_length)
    print("*" * len(password))


def get_valid_password(minimum_length):
    """Prompt user for password that meets minimum length requirements."""
    password = input("Set password: ")
    while len(password) < minimum_length:
        print(f"Password must be a minimum of {minimum_length} characters.")
        password = input("Password: ")
    return password


main()
