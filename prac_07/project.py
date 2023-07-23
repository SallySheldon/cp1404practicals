"""
CP1404 Practical 07 - Do-from-scratch Exercise
Project Management Program
Estimated time to complete: 45 mins
Actual time to complete:

Project class module.
"""


class Project:
    """Define a Project class."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """Initialise a Project object with attributes:
        name: string
        start_date: date
        priority: integer
        cost_estimate: float
        percent_complete: integer
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        """Return a string representation of a Project object."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: $" \
               f"{self.cost_estimate:.2f}, completion: {self.percent_complete}%"

    def __repr__(self):
        """Return official representation of a Project object as string representation."""
        return str(self)

    def __lt__(self, other):
        """Rank Project objects in order of priority."""
        return self.priority < other.priority

    def __eq__(self, other):
        """Determine whether Project objects have equal priority."""
        return self.priority == other.priority

    def is_complete(self):
        """Determine whether a Project object is complete."""
        return self.percent_complete == 100

    # TODO: Is a method required to sort Projects by date?


def run_tests():
    """Test methods in Project class using dummy data."""
    read_7_habits_book = Project("Read 7 Habits Book", "13/12/2021", 6, 99.0, 100)
    build_car_park = Project("Build Car Park", "12/09/2021", 2, 600000.0, 95)
    mow_lawn = Project("Mow Lawn", "31/10/2022", 3, 3.0, 0)
    projects = [read_7_habits_book, build_car_park, mow_lawn]

    print("The unsorted project list is: ")
    for project in projects:
        print(project)

    print(f"\nThe priority-sorted project list should be in order: \n"
          f"{build_car_park.name}, {mow_lawn.name}, {read_7_habits_book.name}.\n"
          f"The test priority-sorting of the list returns: ")
    projects.sort()
    for project in projects:
        print(project)

    print(f"\nThe completed project list should be {read_7_habits_book.name}. The test method returns: ")
    for project in projects:
        if project.is_complete():
            print(project.name)


if __name__ == "__main__":
    run_tests()
