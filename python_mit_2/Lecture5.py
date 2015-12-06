def iter_power(base, exp):
    """
    base can be float or int, exp is an int >=0
    returns an int or float y such as y = base ** exp
    """
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


def recurPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    return base * recurPower(base, exp - 1)


def recurPowerNew(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    """
    if exp == 0:
        return 1.0
    else:
        if exp % 2 == 0:
            return recurPowerNew(base * base, exp / 2)
        return base * recurPowerNew(base, exp - 1)


def recurPowerNew2(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    """
    if exp == 0:
        return 1.0
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    else:
        return base * recurPowerNew(base, exp - 1)


def gcdIter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    for test in range(min(a, b), 0, -1):
        if a % test == 0 and b % test == 0:
            return test


def gcdRecur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


def lenIter(aStr):
    """
    aStr: a string

    returns: int, the length of aStr
    """
    count = 0
    for c in aStr:
        count += 1
    return count


def lenRecur(aStr):
    """
    aStr: a string

    returns: int, the length of aStr
    """
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])


def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        if char == aStr:
            return True
        return False
    else:
        # Find middle character index
        # mid_index = 0
        if len(aStr) % 2 == 0:
            mid_index = int(len(aStr) / 2)
        else:
            mid_index = int((len(aStr) - 1) / 2)
        if char == aStr[mid_index]:
            return True
        elif char < aStr[mid_index]:
            return isIn(char, aStr[:mid_index])
        else:
            return isIn(char, aStr[mid_index:])
def main():
    # print(iter_power(-6.66, 2))
    # print(recurPowerNew(-6.92, 2))
    # print(gcdIter(17, 12))
    # print(gcdRecur(6, 12))
    # print(lenIter('sfdf r'))
    # print(lenRecur('abcderete'))
    print(isIn('m', 'abcdddxxxx'))


if __name__ == '__main__':
    main()
