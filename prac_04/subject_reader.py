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
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject details from a nested list in sentence form."""
    for record in data:
        print(f"{record[0]} is taught by {record[1]} and has {record[2]} students")


main()
