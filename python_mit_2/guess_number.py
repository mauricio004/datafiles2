low = 0
high = 100
number = (low + high) / 2
guess_status = ''

print("Please think of a number between 0 and 100!")
while (guess_status != 'c'):
    number = (low + high) / 2
    print("Is your secret number " + str(number) + "?")
    guess_status = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if guess_status == 'l':
        low = number
    elif guess_status == 'h':
        high = number
    elif guess_status == 'c':
        break
    else:
        print("Sorry, I did not understand your input")
print("Game over. Your secret number was: "+str(number))
        
    

                            