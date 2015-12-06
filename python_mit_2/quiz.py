def evalQuadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    """
    return a * (x ** 2) + b * x + c


def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    """
    return evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)


def primesList(N):
    """
    N: an integer
    Returns a list of prime numbers
    """
    # Your code here
    p = []
    for i in range(2, N + 1):
        test = True
        if i == 2:
            p.append(i)
        elif i % 2 == 1:
            for k in range(2, i):
                if i % k == 0:
                    test = False
            if test is True:
                p.append(i)
    p.sort()
    return p

def genPrimes():
    """
    N: an integer
    """
    # Your code here
    # Your code here
    x = 2
    p = []
    while True:
        test = True
        if x == 2:
            p.append(x)
            yield x
        elif x % 2 == 1:
            for k in p:
                if x % k == 0:
                    test = False
            if test is True:
                p.append(x)
                yield x
        x += 1


def runprimeList(N, primesList):
    print(primesList(N))


def count7(N):
    """
    N: a non-negative integer
    """
    if len(str(N)) == 1:
        if str(N) == '7':
            return 1
        return 0
    return count7(N // 10) + count7(N % 10)


def factR(n):
    if n == 1:
        return n
    return n * factR(n - 1)


def uniqueValues(aDict):
    """
    aDict: a dictionary
    """
    # Create a list with all values
    v_dict = {}
    # Create dict to count the integers
    for k in aDict.keys():
        if aDict[k] not in v_dict:
            v_dict[aDict[k]] = 1
        else:
            v_dict[aDict[k]] += 1

    # Create list with unique values
    unique_values_list = []
    for j in v_dict.keys():
        if v_dict[j] < 2:
            unique_values_list.append(j)

    # Create list with unique keys
    unique_keys_list = []
    for q in aDict.keys():
        if aDict[q] in unique_values_list:
            unique_keys_list.append(q)
    unique_keys_list.sort()

    return unique_keys_list


def rununiqueValues(aDict, uniqueValues):
    print(aDict)
    print(uniqueValues(aDict))
    print()


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    L_copy = L[:]
    for i in L_copy:
         if not f(i):
            L.remove(i)
    return len(L)


def run_satisfiesF(L, satisfiesF):
    print(satisfiesF(L))
    print(L)


def f(s):
    return 'd' in s


def main():
    # Problem 4
    # print(evalQuadratic(-1, -3, -12, -3))
    # print(twoQuadratics(-1, -0.24, 5, 0, 1, 3, 5, 0))

    # Problem 5
    #N = 4
    #runprimeList(N, primesList)
    # N = 19
    # runprimeList(N, primesList)
    # N = 185
    # runprimeList(N, primesList)

    foo = genPrimes()
    print(foo.next())
    print(foo.next())
    print(foo.next())
    print(foo.next())
    print(foo.next())
    print(foo.next())
    print(foo.next())
    print(foo.next())
    print(foo.next())
    print(foo.next())



    # print(factR(5))
    # print(count7(4581))

    # Problem #7
    # d = {'a': 21, 'b': 20, 'c': 21, 'd': 3, 'e': 26}
    # rununiqueValues(d, uniqueValues)
    # d = {1: 21, 2: 20, 3: 21, 4: 3, 5: 26}
    # rununiqueValues(d, uniqueValues)
    # d = {'a': 21, 'b': 20, 'c': 21, 'd': 20, 'e': 21}
    # rununiqueValues(d, uniqueValues)
    # d = {}
    # rununiqueValues(d, uniqueValues)

    # Problem #8
    # L = ['a', 'b', 'a']
    # run_satisfiesF(L, satisfiesF)
    # L = ['a', 'b', 'a', 'x', 'd']
    # run_satisfiesF(L, satisfiesF)
    # L = []
    # run_satisfiesF(L, satisfiesF)

if __name__ == '__main__':
    main()