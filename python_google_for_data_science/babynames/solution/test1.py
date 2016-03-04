__author__ = 'MFlores1'

import re
def practice():
    text = 'My phone number is 345-343-4546 and also my other phone 3433435098'
    pattern = '\d+\W\d+\W\d+'
    match = re.findall(r'\d+\W*\d+\W*\d+', text)

    if match:
        for m in match:
            print m

    else:
        print 'no match'


practice()