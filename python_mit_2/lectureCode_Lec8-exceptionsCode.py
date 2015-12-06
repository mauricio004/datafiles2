def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as err:
        print("division by zero! " + str(err))
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


def divideNew(x, y):
    try:
        result = x // y
    except ZeroDivisionError as err:
        print("division by zero! " + str(err))
    except TypeError:
        divideNew(int(x), int(y))
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


def openfile():
    try:
        f = open('grades.txt')
    except:
        raise Exception('Can not open grades file')
    finally:
        print("Please check")


def main():
    #divideNew('3', '4')
    openfile()
if __name__ == '__main__':
    main()