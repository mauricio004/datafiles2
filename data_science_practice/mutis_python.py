__author__ = 'MFlores1'

from random import randint


def guess_number():

    secret_number = randint(0, 10)
    # secret_number = 7
    guess = -1
    count = 1
    while secret_number != guess:
        guess = int(raw_input('Please guess an integer between 0 and 100: '))
        print('secret number:', secret_number)
        print('count:', count)

        if count > 4:
            break
        elif guess < secret_number:
            print('your guess is low')
        elif guess > secret_number:
            print('your guess is high')
        else:
            print('you guessed right!')

        count += 1


def guess_number2():

    secret_number = randint(0, 100)
    # secret_number = 7
    guess = -1
    count = 1
    while count <= 10:
        guess = int(raw_input('Please guess an integer between 0 and 100: '))
        print('secret number:', secret_number)
        print('count:', count)

        if guess < secret_number:
            print('your guess is low')
        elif guess > secret_number:
            print('your guess is high')
        else:
            print('you guessed right!')
            break
        count += 1

    if secret_number == guess:
        print('You won!')
    else:
        print('You lost')


from random import randint


def guess_number3():

    secret_number = randint(0, 100)
    guess = -1
    count = 1
    while count <= 10:
        guess = int(raw_input('Please guess an integer between 0 and 100: '))

        if guess < secret_number:
            print('Your guess is low')
        elif guess > secret_number:
            print('Your guess is high')
        else:
            print('You guessed right!')
            break
        count += 1

    if secret_number == guess:
        print('You won!')
    else:
        print('You lost')

if __name__ == '__main__':
    guess_number3()