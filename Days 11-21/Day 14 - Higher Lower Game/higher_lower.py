import random
from art import logo, vs
from data import data


def get_the_options(score, correct_answer):
    if score > 0:
        first_option = correct_answer
        second_option = random.choice(data)
    else:
        first_option, second_option = random.sample(data, 2)
    return first_option, second_option


def get_correct_answer(first_option, second_option):
    return first_option if first_option[
        "follower_count"] > second_option["follower_count"] else second_option


def let_user_guess(first_option, second_option):
    print(
        f"Compare A: {first_option["name"]}, {first_option["description"]}, {first_option["country"]}")
    print(vs)
    print(
        f"Against B: {second_option["name"]}, {second_option["description"]}, {second_option["country"]}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    return user_choice


def did_user_guess(user_choice, score, continue_game):
    if (user_choice == "a" and correct_answer == first_option) or (user_choice == "b" and correct_answer == second_option):
        print(f"Yeah, that's right! Current score: {score}")
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False
    return score, continue_game


score = 0
continue_game = True
first_option, second_option, correct_answer = ({}, {}, {})

while continue_game:
    print(logo)
    first_option, second_option = get_the_options(score, correct_answer)
    correct_answer = get_correct_answer(first_option, second_option)
    user_choice = let_user_guess(first_option, second_option)
    score, continue_game = did_user_guess(user_choice, score, continue_game)
