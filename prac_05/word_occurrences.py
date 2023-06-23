"""
CP1404 Practical 05
Do-from-scratch Exercises
Word Occurrences
Estimate:   10 minutes
Actual:     20 minutes
"""

text = input("Text: ").lower()
words = text.split()
words_to_occurrences = {}
for word in words:
    try:
        words_to_occurrences[word] += 1
    except KeyError:
        words_to_occurrences[word] = 1
for word, occurrences in sorted(words_to_occurrences.items()):
    print(f"{word} : {occurrences}")
