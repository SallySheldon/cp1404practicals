"""
CP1404 Practical 05
Do-from-scratch Exercises
Word Occurrences
Estimate:   10 minutes
Actual:     18 minutes
"""

text = input("Text: ").lower()
words = text.split()
words_to_occurrences = {}
for word in words:
    try:
        words_to_occurrences[word] += 1
    except KeyError:
        words_to_occurrences[word] = 1
maximum_width = max((len(word) for word in words_to_occurrences))
for word, occurrences in sorted(words_to_occurrences.items()):
    print(f"{word:{maximum_width}} : {occurrences}")
