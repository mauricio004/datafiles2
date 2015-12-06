# coding=utf-8
def getSubLists(L, n):
    """
    (list, int) -> list

    Returns a list of all possible sublists in L of length n without
    skipping elements in L.  The sublists in the returned list should
    be ordered in the way they appear in L, with thoses sublists starting
    from a smaller index being at the front of the list
    """
    lst = []
    for index, value in enumerate(L):
        sublst = []
        for j in range(index, index + n):
            if index <= len(L) - n:
                sublst.append(L[j])
        if len(sublst) > 0:
            lst.append(sublst)
    return lst


def longestRun(L):
    """
    (list) - > int

    Returns the length fo the longest run of monotonically increasing numbers
    occurring in L.
    """
    maxm = 0
    for m in range(len(L), 0, -1):
        lst = getSubLists(L, m)
        for index, sublst in enumerate(lst):
            sorted = True
            for i in range(len(sublst) - 1):
                if sublst[i + 1] < sublst[i]:
                    sorted = False
                    break
            if sorted:
                if m > maxm:
                    maxm = m
    return maxm


def longestRun2(L):
    """
    (list) - > int

    Returns the length fo the longest run of monotonically increasing numbers
    occurring in L.
    """
    maxm = 0
    for m in range(len(L), 0, -1):
        lst = []
        for index, value in enumerate(L):
            sublst = []
            for j in range(index, index + m):
                if index <= len(L) - m:
                    sublst.append(L[j])
            if len(sublst) > 0:
                lst.append(sublst)

        for index, sublst in enumerate(lst):
            sorted = True
            for i in range(len(sublst) - 1):
                if sublst[i + 1] < sublst[i]:
                    sorted = False
                    break
            if sorted:
                if m > maxm:
                    maxm = m
    return maxm


class Person(object):
    def __init__(self, name):
        # create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None

    def getLastName(self):
        # return self's last name
        return self.lastName

    def setAge(self, age):
        # assumes age is an int greater than 0
        # sets self's age to age (in years)
        self.age = age

    def getAge(self):
        # assumes that self's age has been set
        # returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        # return True if self's name is lexicographically less
        # than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        # return self's name
        return self.name


class USResident(Person):
    """
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status.lower() in ('citizen', 'legal_resident', 'illegal_resident'):
            self.status = status
        else:
            raise ValueError("Error in input")

    def getStatus(self):
        """
        Returns the status
        """
        return self.status


class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None

    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before

    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def myName(self):
        return self.name

    def __str__(self):
        return self.after


def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    # Insert at the end
    if newFrob.name > atMe.name:
        newFrob.setBefore(atMe.name)
        atMe.setAfter(newFrob)
    else:
        atMe.setBefore(newFrob.name)
        newFrob.setAfter(atMe.name)


if __name__ == '__main__':
    frobs = []
    eric = Frob('eric')
    frobs.append(eric)
    andrew = Frob('andrew')
    frobs.append(andrew)
    ruth = Frob('ruth')
    frobs.append(ruth)
    fred = Frob('fred')
    frobs.append(fred)
    martha = Frob('martha')
    frobs.append(martha)
    boy = Frob('boy')
    for f in frobs:
        print str(f)

    insert(eric, andrew)



    print "--Eric--"
    print eric.getBefore()
    print eric.getAfter()
    print "--andrew--"
    print andrew.getBefore()
    print andrew.getAfter()
    insert(eric, ruth)
    print "--ruth--"
    print ruth.getBefore()
    print ruth.getAfter()


