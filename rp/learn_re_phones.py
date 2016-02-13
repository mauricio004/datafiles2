__author__ = 'MFlores1'


import re


def text_re(txt):

    phone_match = re.search(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d'
                            r'{4})',
                            txt, re.DOTALL)

    # phone_match = re.search(r'(ddd ddd dddd)', txt, re.DOTALL)
    if phone_match:
        p = phone_match.group(1).strip()
        print p
    else:
        print 'No match'


if __name__ == '__main__':
    # Need to search for the number below too without characters between numbers
    # 123 456 6677
    text = 'This is a  123 apt4 road canyon sample with multiple phone numbers like (415)235 4579 yes tsisi MMM  sdfd'

    text_re(text)

