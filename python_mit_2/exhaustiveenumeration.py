
def squareroot(x):
    epsilon = 0.01
    step = epsilon ** 2
    numguesses = 0
    ans = 0.0
    while abs(ans ** 2 - x) >= epsilon and ans * ans <= x:
        ans += step
        numguesses += 1
    print('numguesses = ' + str(numguesses))
    print('ans : ' + str(ans))
    if abs(ans ** 2 - x) >= epsilon:
        print('Failed on square root of', str(x))
    else:
        print(str(ans) + ' is close to square root of ' + str(x))


def main():
    squareroot(0.5)

if __name__ == '__main__':
    main()