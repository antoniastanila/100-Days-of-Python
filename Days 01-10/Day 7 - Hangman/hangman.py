import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

# print(chosen_word)
print("Word to guess: ", end="")
for letter in chosen_word:
    print("_", end="")

print("\n")

game_over = False
lives = 6
correct_letters = []

while not game_over:
    print(
        f"************************************* {lives}/6 LIVES LEFT *************************************")
    print("\n")
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word and guess not in correct_letters:
        correct_letters.append(guess)
    elif guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ''
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    print("\n")
    if guess not in chosen_word:
        print(
            f"You guessed {guess}, but it's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(
                "***  Y O U   L O S T  ***")
            print(
                f"***  The word was: {chosen_word}  ***")

    if "_" not in display:
        game_over = True
        print("***  Y O U   W O N  ***")

    print(hangman_art.stages[lives])
