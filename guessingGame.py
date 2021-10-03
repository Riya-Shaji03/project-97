import random
print('Number guessing Game')
# randint function to generate a random nuber from 1 to 9
number = random.randint(1,9)
chances = 0
while (chances < 5):
    chances = chances +1
    guess = int(input('Enter your number'))
    if(guess == number):
        print('congrtulations You Win!')
    elif(guess<number):
        print('Your guess was too low.')
    else:
        print('Your guess was too high.')
if not (chances < 5):
    print('You Lose! The number is', number)
    


