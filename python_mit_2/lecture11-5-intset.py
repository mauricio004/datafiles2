class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers
        """
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """Returns a new intSet containing the elements that appear
            in self and other intSets"""
        s = intSet()
        for v in self.vals:
            if v in other.vals:
                s.insert(v)
        return s

    def __len__(self):
        """Returns the number of elements in self"""
        #return len(self.vals)
        return 1

a = intSet()
b = intSet()
a.insert(1)
a.insert(2)
a.insert(3)
b.insert(2)
b.insert(2)

c = a.intersect(b)

print(len(a))
#b.__len__()
#print(len(a))
#s = intSet()
#print(s)
#s.insert(3)
#s.insert(4)
#s.insert(3)
#print(s)
#print(s.member(3))
#print(s.member(5))
#print(s.insert(6))
#print(s)
#s.remove(3)
#print(s)

