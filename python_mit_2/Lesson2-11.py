varA = 15 # integer
varB = 10 # string

if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
elif varA < varB:
    print('smaller')