import random
from guess_the_number_art import logo

NUMBER_TO_GUESS = random.randint(1, 100)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
number_was_guessed = False


def make_guess():
    global number_was_guessed
    guess = int(input("Make a guess "))
    if guess < NUMBER_TO_GUESS:
        print("Too low.")
        print("Guess again.")
    elif guess > NUMBER_TO_GUESS:
        print("Too high.")
        print("Guess again.")
    else:
        number_was_guessed = True
        print(f"You got it! The number was {NUMBER_TO_GUESS}.")
    return guess


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print(logo)

print("Welcome to number guessing game!")
print("I'm thinking of a number between 1 and 100.")

attempts = set_difficulty()
while attempts > 0:
    print(f"You have {attempts} attempts renaining to guess the number.")
    if make_guess() == NUMBER_TO_GUESS:
        break
    attempts -= 1

if number_was_guessed == False:
    print(f"You ran out of guesses... The number was {NUMBER_TO_GUESS}")
