__author__ = 'MFlores1'

import random


def draw_balls():
    """
    0 = red balls
    1 = green balls

    """

    # Need to remove winning ball
    return random.choice([0, 0, 0, 1, 1, 1])


def no_replacement_simulation(num_trials):
    num_wins = 0.0
    for i in range(num_trials):
        previous = 0
        for j in range(3):
            d = draw_balls()
            total = d + previous
            previous = d
            if total == 0 or total == 3:
                num_wins += 1
