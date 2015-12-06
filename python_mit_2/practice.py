# coding=utf-8


def sharp(x):
    """
    (int) -> int
    x: an integer number >= 2

    Returns the value of x# such as
    x# = ((((((2 ^ 3) ^ 4) ^ 5) …) …) x-1) ^ x)
    """
    if type(x) != int:
        raise TypeError("sharp accepts int arguments, %s given" % type(x))

    assert x >= 2, "sharp accepts integers >= 2"

    if x == 2:
        return 2
    return sharp(x - 1) ** x


def ndigits(x):
    """
    (int) -> int

    Returns the number of digits in the integer
    x recursively
    """
    if len(str(x)) == 1:
        return 1
    return ndigits(x // 10)


def nfruits(dict_of_fruits, pattern):
    """
    Assumes dict_of_fruits is a dictionary and pattern is a str
    Returns an integer.
    """
    pattern_list = list(pattern)
    for p in pattern_list:
        if p in dict_of_fruits:
            dict_of_fruits[p] -= 1
        for f in dict_of_fruits:
            if f != p and len(pattern_list) != 1:
                dict_of_fruits[f] += 1
        pattern_list = pattern_list[1:]
    return max(dict_of_fruits.values())


if __name__ == '__main__':
    # print ndigits(sharp(7)) + 2 *ndigits(sharp(6)) + ndigits(sharp(5)) + ndigits(sharp(4))
    print nfruits({'A': 5, 'B': 7, 'C': 8, 'D': 11, 'E': 4}, 'AAABBBEECAAABBAACCAADDBBAACDCAAABBBAEACCAEADABCB')