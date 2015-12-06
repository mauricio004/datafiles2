# lecture 3.1, slide 2

# repetitive addition

def test():
    x = 3
    ans = 0
    itersLeft = x
    while (itersLeft != 0):
        ans = ans + x
        itersLeft = itersLeft -1
    print(str(x) + '*' + str(x) + ' = ' +str(ans))

def main():
    test()

if __name__ == '__main__':
    main()