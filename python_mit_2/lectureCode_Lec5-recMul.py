def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)

def main():
    print(recurMul(2,2))

if __name__ == '__main__':
    main()
