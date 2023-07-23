"""
CP1404 Practical 07 - Do-from-scratch Exercise.
Project Management Program client code.
"""

from project import Project

DEFAULT_FILENAME = "projects.txt"

MENU = "- (L)oad projects\n" \
       "- (S)ave projects\n" \
       "- (D)isplay projects\n" \
       "- (F)ilter projects by date\n" \
       "- (A)dd new project\n" \
       "- (U)pdate project\n" \
       "- (Q)uit"


def main():
    """Project management program to load and save a data file and use a list of Project objects."""
    print(MENU)
    projects = load_projects(DEFAULT_FILENAME)  # Load initial projects from default file
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = get_filename("Enter the name of a file to load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = get_filename("Enter the name of a file to save projects to: ")
            # save_projects(filename)
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            # filter_projects(projects)
            pass
        elif choice == "A":
            # add_project(projects):
            pass
        elif choice == "U":
            # update_project(projects)
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def get_filename(prompt):
    """Prompt user for a file name, using a default filename if user inputs a blank."""
    filename = input(prompt)
    if filename == "":
        filename = DEFAULT_FILENAME  # Use default filename if user inputs a blank string
    return filename


def load_projects(filename):
    """Load a data file of project details, saving each project as a list of Project objects."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip header line
        for line in in_file:
            # File format is: Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage
            parts = line.strip().split('\t')
            # Construct a Project object using the elements
            # Start Date = date, Priority = int, Cost Estimate = float, Completion Percentage = int
            # TODO: reformat date from string using datetime
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(filename):
    """Save Project details to file."""


def display_projects(projects):
    """Display stored Project objects as Incomplete and Completed projects, sorted by priority order."""
    projects.sort()  # Sort projects by priority order
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"  {project}")
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print(f"  {project}")


def filter_projects(projects):
    """Filter list of Project objects by date."""


def add_project(projects):
    """Add a new Project object to a list of stored Projects."""


def update_project(projects):
    """Update Priority and/or Completion Percentage details for a stored Project object. """


main()
