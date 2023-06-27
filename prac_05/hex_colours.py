"""
CP1404 - Practical 05
Based on the state name example program above, create a program that allows you to look up hexadecimal colour codes
like those at http://www.color-hex.com/color-names.html
Use a constant dictionary of about 10 colour names and write a program that allows a user to enter a name and get the
code, e.g., entering AliceBlue (or aliceblue - make it case-independent) should show #f0f8ff.
Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.
"""

COLOUR_TO_CODE = {'aliceblue': '#f0f8ff', 'amaranth': '#e52b50', 'aquamarine1': '#7fffd4', 'aureolin': '#fdee00',
                  'bisque2': '#eed5b7', 'emerald': '#50c878', 'fuchsia rose': '#c74375', 'harlequin': '#3fff00',
                  'imperial red': '#ed2939', 'mandarin': '#f37a48', 'ochre': '#cc7722'}

print(COLOUR_TO_CODE)

colour_name = input("\nEnter colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name.title()} is colour code {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Sorry, that colour name isn't in our list.")
    colour_name = input("\nEnter colour name: ").lower()
