"""
CP1404 Practical 07 - Do-from-scratch Exercise.
Project Management Program client code.
"""

from datetime import datetime

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
            save_projects(filename, projects)
            print(f"{len(projects)} projects saved to {filename}.")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            print("Let's add a new project.")
            add_project(projects)
        elif choice == "U":
            update_project(projects)
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
            # Construct a Project object using the elements:
            # Start Date = date, Priority = int, Cost Estimate = float, Completion Percentage = int
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save Project details to file."""
    with open(filename, 'w') as out_file:
        for project in projects:
            print(project.name, project.start_date, project.priority, project.cost_estimate,
                  project.percent_complete, sep="\t", file=out_file)


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
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    # Create a list of the start dates of projects that are after the filter date
    filtered_project_start_dates = []
    for project in projects:
        if project.start_date > filter_date:
            filtered_project_start_dates.append(project.start_date)
    filtered_project_start_dates.sort()  # Sort the filtered project start_dates in ascending order
    for filtered_project_start_date in filtered_project_start_dates:
        for project in projects:
            if project.start_date == filtered_project_start_date:
                print(project)
    # NOTE: Because the __lt__() method in the Project class definition is already defining the < comparison by
    # reference to the project.priority attribute, I can't redefine that method to sort by the
    # project.start_date attribute.
    # Another option might have been to sort the projects list by start_date using a lambda function (but we haven't
    # learned these so far):
    # projects = sorted(projects, key=lambda x: x.start_date)
    # for project in projects:
    #     if project.start_date > filter_date:
    #         print(project)


def add_project(projects):
    """Add a new Project object to a list of stored Projects."""
    name = get_valid_string("Name: ")
    start_date = get_valid_string("Start date (dd/mm/yyyy): ")
    priority = get_valid_integer("Priority: ")
    cost_estimate = get_valid_float("Cost estimate: $")
    percent_complete = get_valid_integer("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    """Update Priority and/or Completion Percentage details for a chosen Project object."""
    # Display numbered list of existing projects
    max_width_index = len(str(len(projects)))  # Calculate alignment value for project numbers
    for i, project in enumerate(projects):
        print(f"{i:{max_width_index}} {project}")
    # Get user choice of project to update
    project_choice = get_valid_integer("Project choice: ")
    # Ensure user choice is not greater than the available project numbers
    while project_choice > len(projects) - 1:
        print("Invalid project choice")
        project_choice = get_valid_integer("Project choice: ")
    print(projects[project_choice])
    # Prompt user to update details; blank inputs retain existing values
    new_percentage = get_valid_integer("New Percentage: ")
    if new_percentage != "":
        new_percentage = int(new_percentage)
        projects[project_choice].percent_complete = new_percentage
    new_priority = get_valid_integer("New Priority: ")
    if new_priority != "":
        new_priority = int(new_priority)
        projects[project_choice].priority = new_priority


def get_valid_string(prompt):
    """Prompt the user for a non-empty string."""
    string = input(prompt)
    while string == "":
        print("Input cannot be blank")
        string = input(prompt)
    return string


def get_valid_integer(prompt):
    """Prompt the user for an integer >= 0."""
    is_valid_input = False
    while not is_valid_input:
        try:
            integer = int(input(prompt))
            if integer < 0:
                print("Number must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid integer")
    return integer


def get_valid_float(prompt):
    """Prompt the user for a float value >= 0."""
    is_valid_input = False
    while not is_valid_input:
        try:
            float_value = float(input(prompt))
            if float_value < 0:
                print("Number must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return float_value


main()
