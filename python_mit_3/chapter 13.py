__author__ = 'MFlores1'
import random

class Location(object):
    def __init__(self, x, y):
        """" x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """ deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        distX = self.x - ox
        distY = self.y - oy
        return ((distX ** 2) + (distY ** 2)) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Drunk already in field')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        currentLocation = self.drunks[drunk]
        x, y = drunk.takeStep()
        self.drunks[drunk] = currentLocation.move(x, y)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name=None):
        """ Name is a string"""
        self.name = name

    def __str__(self):
        if self.name != 'None':
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoice = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoice)


def walk(f, d, numSteps):
    """ f is a field, d a drunk and numSteps an int >=0
    Moves d numSteps, and return the difference between the location
    at the start of the walk and the final location.
    """
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

