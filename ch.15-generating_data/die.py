import random

class Die:
    """Representation of a single die."""

    def __init__(self, num_sides=6):
        """The default being a 6-sided dice."""
        self.num_sides = num_sides
        
    def roll(self):
        """Random value between 1 - < num_sides >, simulating a dice roll."""
        return random.randint(1, self.num_sides)