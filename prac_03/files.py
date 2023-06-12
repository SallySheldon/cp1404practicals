"""
CP1404 - Practical 03
Do-from-scratch Exercises
Files
"""

# 1. Write code that asks the user for their name, then opens a file called
# "name.txt" and writes that name to it. Remember to close your file.
name = input("What is your name? ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. (In the same file, but as if it were a separate program) Write code that
# opens "name.txt" and reads the name (as above) then prints, "Your name is
# Bob" (or whatever the name is in the file).

# Version 1: in_file = open(filename) method
in_file = open("name.txt")
# .strip() is not needed as \n character is not a problem for required output
name = in_file.read()  # .read() method
# name = in_file.readline()  # .readline() method
# name = in_file.readlines()[0]  # .readlines() method
print(f"Your name is {name}")  # print statement used for above 3 methods
# Alternative `for line in file` method:
# for line in in_file:
#     print(f"Your name is {line}")
in_file.close()

# Version 2: with open(filename) as in_file method
with open("name.txt") as in_file:
    name = in_file.readline()  # or any of the methods in Version 1
print(f"You name is {name}")


# 3. Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and
# adds them together then prints the result, which should be... 59.
in_file = open("numbers.txt")
total = 0
for i in range(2):
    total += int(in_file.readline())
print(total)
in_file.close()

# 4. Now write a fourth block of code that prints the total for all lines in
# numbers.txt or a file with any number of numbers.
in_file = open("numbers.txt")
total = 0
for line in in_file:
    total += int(line)
print(total)
in_file.close()
