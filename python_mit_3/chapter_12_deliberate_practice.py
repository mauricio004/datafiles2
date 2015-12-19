__author__ = 'MFlores1'
import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result += str(rollDie())
    return result

def getTarget(goal):
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries += 1
        if rollN(numRolls) == goal:
            return numTries

def runSim(goal, numTrials):
    result = 0
    for i in range(numTrials):
        result += getTarget(goal)
    avg = result/float(numTrials)
    print 'Average number of tries', avg

print rollN(5)
runSim('11111', 100)