import sys

def Cat(filename):
    try:
        f = open(filename, 'rU')
        text = f.read()
        print('---' + filename)
        print(text)
    except FileNotFoundError:
        print('File not found error' + filename)


# Define a main() function that prints a little greeting
def main():
    args = sys.argv[1:]
    for arg in args:
        Cat(arg)


#  This is the standard boilerplate that calls the main() function
if __name__ == "__main__":
    main()
