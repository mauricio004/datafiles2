def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def main():
    print(iterMul(2,2))

if __name__ == '__main__':
    main()