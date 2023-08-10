"""
CP1404 Practical 10
Wikipedia API & Python Library
"""

import wikipedia


def main():
    """Program to return a summary of a user-entered Wikipedia page."""
    search_string = input("Enter title or search phrase: ")
    while search_string != "":
        try:
            page = wikipedia.page(search_string, auto_suggest=False)
            print(page.summary)
        except wikipedia.DisambiguationError as e:
            print(e.options)
        search_string = input("Enter title or search phrase: ")
    print("Hope this was informative!")


main()
