"""
CP1404 Practical 05
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data file and display details of subject, lecturer and student numbers."""
    subjects_data = get_data()
    print(subjects_data)
    display_subject_details(subjects_data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject details from a nested list in neatly aligned sentence form."""
    # Use length of longest strings for subject code, teacher name and student numbers, as alignment spacing.
    code_alignment = max((len(record[0]) for record in data))
    name_alignment = max((len(record[1]) for record in data))
    number_alignment = max((len(str(record[2])) for record in data))
    for record in data:
        print(f"{record[0]:{code_alignment}} is taught by {record[1]:{name_alignment}} and has "
              f"{record[2]:{number_alignment}} students")


main()
