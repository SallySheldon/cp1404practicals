"""
CP1404 Practical 05
Do-from-scratch Exercises
Word Occurrences
Estimate:   10 minutes
Actual:     18 minutes
"""

word_to_occurrences = {}
text = input("Text: ").lower()
words = text.split()
for word in words:
    try:
        word_to_occurrences[word] += 1
    except KeyError:
        word_to_occurrences[word] = 1
maximum_width = max((len(word) for word in word_to_occurrences))
for word, occurrences in sorted(word_to_occurrences.items()):
    print(f"{word:{maximum_width}} : {occurrences}")
