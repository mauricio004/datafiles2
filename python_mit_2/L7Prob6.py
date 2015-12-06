def f(n):
    """
    n: integer, n >= 0.
    """
    if n == 0:
        return n
    else:
        return n * f(n-1)


def main():
    print(f(3))

if __name__ == '__main__':
    main()



