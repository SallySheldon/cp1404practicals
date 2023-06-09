"""
CP1404 - Prac 02 - Extension - More temperatures
Program to convert temperatures from input file
"""

MENU = """
Choose conversion required:
(C)elsius to Fahrenheit
(F)ahrenheit to Celsius
"""


def main():
    """Program to convert temperatures from input file between Celsius and
    Fahrenheit and save to output file."""
    in_file = open("temps_input.txt")
    out_file = open("temps_output.txt", "w")
    print(MENU)
    choice = input(">>> ").upper()
    for line in in_file:
        temperature_in = float(line)
        if choice == "C":
            temperature_out = convert_celsius_to_fahrenheit(temperature_in)
        else:
            temperature_out = convert_fahrenheit_to_celsius(temperature_in)
        print(temperature_out, file=out_file)
    out_file.close()


def convert_celsius_to_fahrenheit(celsius):
    """Convert degrees celsius to degrees fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert degrees fahrenheit  to degrees celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


main()
