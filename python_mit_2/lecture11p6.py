class Queue (object):

    def __init__(self):
        self.vals = []

    def insert(self, e):
        self.vals.append(e)

    def remove(self):
        try:
            v = self.vals[0]
            self.vals.pop(0)
        except:
            raise ValueError
        return v

q = Queue()
q.insert(5)
q.insert(6)
q.remove()
q.insert(7)
q.remove()
print(q.remove())
#q.remove()
print(q.vals)
