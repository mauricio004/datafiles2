__author__ = 'MFlores1'

import random

#
# def draw_balls(previous):
#     """
#     0 = red balls
#     1 = green balls
#     """
#
#     if previous != '':
#         balls_list.remove(previous)
#     return random.choice(balls_list)


def no_replacement_simulation(num_trials):
    num_wins = 0.0
    for i in range(num_trials):
        balls_list = ['b', 'b', 'b', 'g', 'g', 'g']
        drawing_balls_lst = []
        for j in range(3):
            d = random.choice(balls_list)
            drawing_balls_lst.append(d)
            # balls_list.remove(d)
        green_count = drawing_balls_lst.count('g')
        black_count = drawing_balls_lst.count('b')
        # P(green) or P(black) = P(green) + P(black)
        if green_count == 3 or black_count == 3:
            num_wins += 1
    r = num_wins / num_trials
    return r

print no_replacement_simulation(10000)