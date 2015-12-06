def isvowel(char):
    char = char.lower()
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

def isvowel2(char):
    char = char.lower()
    if char in 'aeiou':
        return True
    else:
        return False


def main():
    print(isvowel2('A'))

if __name__ == '__main__':
    main()