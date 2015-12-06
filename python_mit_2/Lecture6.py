__author__ = 'MFlores1'
def oddTuples(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    """
    t = ()
    i = -1
    for a in aTup:
        i += 1
        if i % 2 == 0:
            t = t + (aTup[i],)
    return t

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def timesFive(a):
    return a * 5

def absolute(a):
    if a < 0:
        return -a
    return a
def addition(a):
    if a < 9:
        return a + 1
    return a - 17

def multip(a):
        return a * a


def howMany(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    """
    count = 0
    for k in aDict.keys():
        count += len(aDict[k])
    return count


def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    d = {}
    for k in aDict.keys():
            d[k] = len(aDict[k])
    big = 0
    bigkey = ''
    for k2 in d.keys():
        if d[k2] > big:
            big = d[k2]
            bigkey = k2
    return bigkey


def biggest2(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    bigkey = None
    biglength = 0
    for k in aDict.keys():
        if len(aDict[k]) >= biglength:
            biglength = len(aDict[k])
            bigkey = k
    return bigkey


def main():
    # print(oddTuples(('a', 'b', 'c', 'd', 4, 3434, 4)))
    # testList = [1, -4, 8, 9]
    # applyToEach(testList, multip)
    # print(testList)
    animals = {}

    print(animals)
    print(biggest2(animals))

if __name__ == '__main__':
    main()