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
            
            x_step, y_step, zero_case_x, zero_case_y = self.get_step()
            if zero_case_x == 0 and zero_case_y == 0:
                continue
                # we avoid moves that lead to nowhere.

            self.x_values.append(x_step)
            self.y_values.append(y_step)

    def get_step(self) -> tuple:
        """
        Refoctirn the fill_walk() so it's lighter
        """
        x_direction = random.choice([1, -1])
        x_distance = random.choice(range(100))
        zero_case_x = x_direction * x_distance
        x_step = self.x_values[-1] + (x_direction * x_distance)

        y_direction = random.choice([1, -1])
        y_distance = random.choice(range(100))
        zero_case_y = y_direction * y_distance
        y_step = self.y_values[-1] + (y_direction * y_distance)

        return x_step, y_step, zero_case_x, zero_case_y
            