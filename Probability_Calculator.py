# Probability Calculator - Victor Freire(devbuda)

import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            return self.contents
        for _ in range(num_balls):
            ball_index = random.randint(0, len(self.contents) - 1)
            drawn_ball = self.contents.pop(ball_index)
            drawn_balls.append(drawn_ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        match = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                match = False
                break

        if match:
            num_successful_experiments += 1

    probability = num_successful_experiments / num_experiments
    return probability
