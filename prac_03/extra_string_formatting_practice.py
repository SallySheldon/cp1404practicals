"""
CP1404 - Prac 03 - Personal extra string formatting practice
"""

# Format alignment of text as in a table arrangement using right align
names = ["Sally Sheldon", "Jack", "Martin Cachard", "Tiny"]
heights = [169, 178, 182, 6]
for i in range(len(names)):
    print(f"{names[i]:>16}{heights[i]:>10}")
print()

# Use center alignment
for i in range(len(names)):
    print(f"{names[i]:^20}{heights[i]:^10}")
print()
