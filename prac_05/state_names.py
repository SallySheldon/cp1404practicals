"""
CP1404 Practical 05
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    # LBYL approach:
    # if state_code in CODE_TO_NAME:
    #     print(state_code, "is", CODE_TO_NAME[state_code])
    # else:
    #     print("Invalid short state")

    # EAFP approach:
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")

    state_code = input("Enter short state: ").upper()
print()  # Print blank line after user exits input mode.

maximum_width = max((len(code) for code in CODE_TO_NAME))
for code in CODE_TO_NAME:
    print(f"{code:<{maximum_width}} is {CODE_TO_NAME[code]}")
