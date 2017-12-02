import random

comGuess = random.randint(0, 100)
while True:
    UserGuess = int(input("Guess a Number between 0-100: "))
    if UserGuess > comGuess:
        print("Guess Lower")
    elif UserGuess < comGuess:
        print("Guess Higher")
    else:
        print("You have guessed the correct number")
        break
