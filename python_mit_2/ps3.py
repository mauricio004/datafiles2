__author__ = 'MFlores1'

import circle

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    """
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    """
    area = 0.0
    bases = [start]
    for i in range(1, int((stop - start) / step)):
        bases.append(bases[i - 1] + step)
    for b in bases:
        rect_area = step * f(b)
        area += rect_area
    return area


def main():
    print(radiationExposure(5, 11, 1))
    # print(f(5))

if __name__ == '__main__':
    main()
