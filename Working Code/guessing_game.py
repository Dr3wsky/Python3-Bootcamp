print('Hello, want to play a little game?')
print('The rules are simple. I will pick a random number, and you will try to guess it.') 
print('To start, if your guess is within 10 of the answer, you will be WARM, if it is more than 1, you will be COLD.')
print('On subsequent turns, you will be WARMER or COLDER based on your last guess.')
print("LET'S PLAY BALL!")

# Inialise import functions, guess tracker and answer
from random import randint
guess_tracker = [0]
ans = randint(1,100)

while True:
    #Prompt User input
    guess = int(input('Enter a number guess between 1 and 100:   '))
    
    #Check if guess is a valid integer
    if guess<1 or guess>100:
        print('OUT OF BOUNDS! Guess again, please enter a valid number.')
        continue
        
    # Run game guess and check
    
    # If first guess is correct, be cheeky and prompt a replay
    if guess == ans:
        print(f"CORRECT!! YOU GUESSED IT IN ONLY {len(guess_tracker)} GUESSES!!")
        break
        
    # If guess incorrect, append to the guess list and give feedback
    guess_tracker.append(guess)
    
    # If it is the first guess, the if below will evaluate to FLASE, and kick to first guess feedback options
    if guess_tracker[-2]:
        if abs(ans-guess)<abs(ans-guess_tracker[-2]):
            print('WARMER...')
        else:
            print('COLDER...')
        
    else:
        if abs(guess-ans)<=10:
            print('WARM!')
        else:
            print('COLD!')
