"""
CP1404 Prac 02
First exercise - Password stars program - Practise committing to Git
"""

MINIMUM_LENGTH = 8


def main():
    """Program to set a password meeting minimum length requirements
    then print as many asterisks as the password has characters."""
    password = get_valid_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_valid_password(minimum_length):
    """Get password that meets minimum length requirements."""
    password = input(f"Set password (minimum of {minimum_length} characters): ")
    while len(password) < minimum_length:
        print(f"Password must be a minimum of {minimum_length} characters.")
        password = input(
            f"Set password (minimum of {minimum_length} characters): ")
    return password


def print_asterisks(sequence):
    """Print as many asterisks as there are characters in supplied sequence."""
    print("*" * len(sequence))


main()
