"""
CP1404 Practical 05
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject_data file and print details of subject, lecturer and student numbers."""
    data = get_data()
    print(data)
    display_subject_details(data)


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
    for i in range(len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students")


main()
