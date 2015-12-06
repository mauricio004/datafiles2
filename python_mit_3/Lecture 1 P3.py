import pylab
import  numpy as np

PATH_TO_FILE = 'julyTemps.txt'


def loadWords():
    inFile = open(PATH_TO_FILE)
    low = []
    high = []
    for line in inFile:
        fields = line.split(' ')
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return low, high


def producePlot(lowTemps, highTemps):
    diffTemps = list(np.array(highTemps) - np.array(lowTemps))
    pylab.plot(range(1, 32), diffTemps)
    pylab.title( 'Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()


if __name__ == '__main__':
    producePlot(loadWords()[0], loadWords()[1])
