import random as rand
secretNumber = rand.randint(1, 10)

def GuessFunc(guessedNumber):
    if guessedNumber > secretNumber:
        return 'You guess is high..'
    elif guessedNumber < secretNumber:
        return 'Your guess is low..'
    elif guessedNumber == secretNumber:
        return f'You guessed it right the SecretNumber is {secretNumber}'
   
def StartPlaying():
    global secretNumber
    secretNumber = rand.randint(1 , 10)
    for i in range(1, 5):
        print("Guess a Number between 1 - 10")
        inputFromUser = int(input())
        result = GuessFunc(inputFromUser)
        print(result)
        if result == f'You guessed it right the SecretNumber is {secretNumber}':
            print("You won 🎉...")
            print('Do you want to play Again? (y/n)')
            status = input()
            playAgainFunc(status)
            return
        else:
            print("Take a Guess again...")
    print("you wasted ALL the chances... You lost😢")   
    

def playAgainFunc(status):
    if status in ('y' , 'yes' , 'Y' , 'Yes'):
     StartPlaying()
    else:
     print("Thanks for playing the game😘..")
     return 
    
StartPlaying()
