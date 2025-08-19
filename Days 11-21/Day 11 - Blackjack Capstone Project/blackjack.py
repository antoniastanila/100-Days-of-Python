from blackjack_art import logo
from blackjack_functions import generate_cards, sum_of_cards

upper_limit = 21
computer_minimum_score = 17

continue_game = True


while continue_game:
    user_cards = []
    user_score = 0

    computer_cards = []
    computer_score = 0

    user_input = input(
        "Do you want to play a game of Blackjack? tyoe 'y' or 'n': ")
    if user_input == "y":

        print(logo)
        user_cards = generate_cards(2, user_cards)
        user_score = sum_of_cards(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        if user_score == upper_limit:
            print("BLACKJACK!! YOU WON!!! ❤️")
        else:
            computer_cards = generate_cards(2, computer_cards)
            computer_score = sum_of_cards(computer_cards)
            print(f"Computer's first card: {computer_cards[0]}")
            if computer_score == upper_limit:
                print("BLACKJACK!! YOU LOST!!! 😨")
            else:
                user_choice = input(
                    "Type 'y' to get another card, type 'n' to pass: ")

                while user_choice == "y":
                    user_cards = generate_cards(1, user_cards)
                    user_score = sum_of_cards(user_cards)
                    if user_score > upper_limit:
                        if 11 in user_cards:
                            user_cards[user_cards.index(11)] = 1
                            user_score -= 10
                        else:
                            print(
                                f"    Your final hand: {user_cards}, final score: {user_score}")
                            print(
                                f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                            print("You went over! You lose. 😭")
                            break
                    print(
                        f"Your cards: {user_cards}, current score: {user_score}")
                    print(f"Computer's first card: {computer_cards[0]}")
                    user_choice = input(
                        "Type 'y' to get another card, type 'n' to pass: ")

                if user_choice == "n":
                    while computer_score < computer_minimum_score:
                        computer_cards = generate_cards(1, computer_cards)
                        computer_score = sum_of_cards(computer_cards)
                    print(
                        f"    Your final hand: {user_cards}, final score: {user_score}")
                    print(
                        f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                    if computer_score < user_score:
                        print("You win! 🥰")
                    if computer_score > upper_limit:
                        print("Opponent went over. You win! 😁")
                        # continue_game = False
                    elif computer_score > user_score:
                        print("You lose! 🙄")
                        # continue_game = False

    elif user_input == "n":
        continue_game = False
    else:
        print("Invalid input.")
