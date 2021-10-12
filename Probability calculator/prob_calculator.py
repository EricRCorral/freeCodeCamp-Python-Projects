import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **args):
        self.contents = []
        for ball in args.keys():
            for i in range(0, args[ball]):
                self.contents.append(ball)

    def draw(self, drawNumber):
        ballsDrawed = []
        if drawNumber < len(self.contents):
            for i in range(0, drawNumber):
                ballsDrawed.append(self.contents.pop(
                    int(random.random() * len(self.contents))))
        else:
            ballsDrawed = self.contents
        return ballsDrawed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = num_experiments
    expected_balls_values = list(expected_balls.values())
    expected_balls_keys = list(expected_balls.keys())

    for i in range(0, num_experiments):
        hatDeepCopy = copy.deepcopy(hat)
        balls_drawed_list: list = hatDeepCopy.draw(num_balls_drawn)
        for i, key in enumerate(expected_balls_keys):
            if balls_drawed_list.count(key) < expected_balls_values[i]:
                num_success -= 1
                break

    return num_success / num_experiments
