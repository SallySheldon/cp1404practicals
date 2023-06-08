"""
CP1404 Prac 02
First exercise - Password stars program - Practise committing to Git
"""

DEFAULT_MINIMUM_LENGTH = 8


def main():
    """Program to ask user to set a password meeting minimum length requirements
    then print asterisks as long as the password."""
    password = get_valid_password(DEFAULT_MINIMUM_LENGTH)
    print_asterisks(password)


def get_valid_password(minimum_length):
    """Prompt user for password that meets minimum length requirements."""
    password = input("Set password: ")
    while len(password) < minimum_length:
        print(f"Password must be a minimum of {minimum_length} characters.")
        password = input("Password: ")
    return password


def print_asterisks(password):
    """Print asterisks as long as a supplied password."""
    print("*" * len(password))


main()
