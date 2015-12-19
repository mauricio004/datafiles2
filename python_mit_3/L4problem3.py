__author__ = 'MFlores1'


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    lenght_lst = []

    if len(L) >= 1:
        for i, val in enumerate(L):
            lenght_lst.append(len(val))
        return stdDev(lenght_lst)
    else:
        return float('NaN')


def stdDev(lst):
    """
    lst: a list of integers

    returns: float, the standard deviation of the list of integers
    """
    mean = sum(lst)/float(len(lst))
    tot = 0.0
    for i, val in enumerate(lst):
        tot += (val - mean) ** 2
    return (tot/len(lst)) ** 0.5

# L = ['a', 'z', 'p']
# L = ['apples', 'oranges', 'kiwis', 'pineapples']
L = ['u', 'kizbjsibiy', 'md', 'fxrklegpwnitp', 'fltyn', 'cvwbcf', 'ehhxudajyltu', 'hxuxa']
print stdDevOfLengths(L)