__author__ = 'MFlores1'
import random, pylab

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


class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoice = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoice)

class EWDrunk(Drunk):
    def takeStep(self):
        stepChoice = [(1.0, 0.0), (-1.0, 0.0)]
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


def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int >= 0, numTrials an int >=0,
    dClass a subclass of Drunk
    Simulates numTrials walks of numSteps steps each.
    Return a list of the final distances for each trial
    """
    Homer = dClass()
    distances = []
    origin = Location(0.0, 0.0)
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(walk(f, Homer, numSteps))
    return distances


def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a sequence of ints >= 0
    numTrials an int > 0, dClass a subclass of Drunk
    For each number of steps in walkLengths, run simWalks with
    numTrials walks and print results
    """
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print dClass.__name__ + ' random walk of', numSteps, 'steps'
        print 'Mean =', sum(distances)/len(distances), 'CV =', CV(distances)
        print 'Max =', max(distances), 'Min =', min(distances)


def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    cvDistances = []
    for numSteps in walkLengths:
        print 'Starting simulation of', numSteps, 'steps'
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials) / float(len(trials))
        meanDistances.append(mean)
        cvDistances.append(CV(trials))
    return meanDistances, cvDistances

def simAll_2(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('b-', 'r:', 'm-. '))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print 'Starting simulation of', dClass.__name__
        means, cvs = simDrunk(numTrials, dClass, walkLengths)
        cvMean = sum(cvs)/float(len(cvs))
        pylab.plot(walkLengths, means)
    pylab.title("Mean Distance from origin")
    pylab.xlabel("Number of steps")
    pylab.ylabel("Distance from origin")
    pylab.legend(loc='best')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()

def simAll_1(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)


def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')


def stdDev(X):
    """"Assumes that X is a list of numbers.
    Returns the standard deviation of X
    """
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot/len(X)) ** 0.5  # Square root of mean difference


class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def main():
    # o = Location(0.0, 0.0)
    # f = Field()
    # d = UsualDrunk("Mauricio")
    # f.addDrunk(d, o)
    # print f.getLoc(d)
    # print walk(f, d, 10000)
    # print f.getLoc(d)

    # drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
    simAll_2((UsualDrunk,), (10, 100, 1000, 10000, 100000), 100)

if __name__ == '__main__':
    main()
