
def countvowels(s):
    s = s.lower()
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
    print('Number of vowels: ' + str(count))


def countbobs(s):
    s = s.lower()
    count = 0
    s2 = s[:]
    index = s2.find('bob')
    while index > -1:
        count += 1
        s2 = s2[index + 2:]
        index = s2.find('bob')
    return count


def longestsubstring(s):
    s = s.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s_temp = ''
    s_final = ''
    alpha_rank = -1
    for c in s:
        s_rank = alpha.find(c)
        if s_rank >= alpha_rank:
            s_temp += c
        else:
            s_temp = ''
            s_temp += c
        alpha_rank = alpha.find(c)
        if len(s_temp) > len(s_final):
            s_final = s_temp
    return s_final


def test():
    for s in ('azcbobobegghakl', 'sfdbobobsdfs', 'abcdef', 'bobsabcde', 'absfsfabcdee', 'abcbcd'):
        print('Test : ' + s + '  Result : ' + longestsubstring(s))


def main():
    #longestsubstring('azcbobobegghakl')
    test()

if __name__ == '__main__':
    main()