import random
import os

def genEven():
    """
    Returns a random number x, where 0 <= x < 100
    """
    lst = []
    for i in range(0, 100):
        if i % 2 == 0:
            lst.append(i)
    return random.choice(lst)


def deterministicNumber():
    """
    Deterministically generates and returns an even number between 9 and 21
    """
    return 10

def stochasticNumber():
    """
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    """
    return random.randrange(9, 21, 2)


def test():
    mylist = []
    random.seed(0)
    for i in xrange(random.randint(1, 10)):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
    print mylist

if __name__ == '__main__':
    test()
