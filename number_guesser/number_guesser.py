import random

lower = 1
upper = 20
max_guesses = 5

num = random.randint(lower, upper)

guesses = 0

while guesses < max_guesses:
    guess = input(f"Guess a number between {lower} and {upper}: ")

    try:
        guess = int(guess)
    except:
        print("Oops! That wasn't a number, try again!")
        continue

    if guess < lower or guess > upper:
        print(f"Try again with a number between {lower} and {upper}!")
    
    if guess == num:
        print(f"Congratulations, you guessed it! The number was {num}.")
        break
    elif guess < num:
        print("Too low, ", end="")
    else:
        print("Too high, ", end="")
    
    guesses += 1
    
    print(f"{max_guesses - guesses} guesses remaining!")
