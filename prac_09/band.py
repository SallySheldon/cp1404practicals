"""Band class for CP1404 Practical 09."""


class Band:
    """Band class."""

    def __init__(self, name=""):
        """Construct a Band with a name and musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band with band name and each musician's details."""
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        band_string = str(", ".join(musician_strings))
        return f"{self.name} ({band_string})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to a band."""
        self.musicians.append(musician)

    def play(self):
        """Return multiline string showing each band musician playing their first (or no) instrument."""
        musician_play_strings = []
        for musician in self.musicians:
            musician_play_strings.append(musician.play())
        return str("\n".join(musician_play_strings))
