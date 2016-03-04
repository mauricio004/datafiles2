__author__ = 'MFlores1'

import re

def practice():
    text = 'Mauricio'

    match = re.search(text, 'Mauricio')

    if match:
        print match.group()
    else:
        print 'no match'


def main():
    print 'text'

if __name__ == '__main__':
    main()