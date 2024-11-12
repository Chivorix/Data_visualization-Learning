import random

class RandomWalk:
    """A class to generate a random walk"""
    def __init__(self, num_points=5000):
        """Starting parameters of the walk"""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """
        Compute the points to be charted,
        completing the lists to be used by pyplot
        """
        while len(self.x_values) < self.num_points:
            x_direction = random.choice([1, -1])
            x_distance = random.choice([0,1,2,3,4])
            x_step = self.x_values[-1] + (x_direction * x_distance)

            y_direction = random.choice([1, -1])
            y_distance = random.choice([1,2,3,4,5])
            y_step = self.y_values[-1] + (y_direction * y_distance)

            if (x_direction * x_distance) == 0 and (y_direction * y_distance) == 0:
                continue
                # we avoid moves that lead to nowhere.

            self.x_values.append(x_step)
            self.y_values.append(y_step)

            