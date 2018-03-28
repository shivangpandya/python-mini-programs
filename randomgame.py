#This is guessing number game

import random
print('Hello. What is your name ? ')
name= input()
secretNumber = random.randint(1,20)
print('Well ' + ' , I am thinnking of a nnumber between 1 and 20')

for guessTaken in range(1,7):
    print('Take a guess.')
    guess= int(input())

    if guess<secretNumber:
        print('Your guess is too low')
    elif guess>secretNumber:
        print('Your guess is too high')
    else:
        break

        #This is for correct statemennt


if guess == secretNumber:
    print('Congratulations' + name + '!You guessed my number correctly')
else:
    print('Sorry' + name + '!The number I was guessing was ' + str(secretNumber))
          
MAa
