import random


def sum_of_cards(cards):
    sum = 0
    for card in cards:
        sum += card
    return sum


def generate_cards(num_of_cards, player_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    while num_of_cards > 0:
        generated_card = random.choice(cards)
        player_cards.append(generated_card)
        num_of_cards -= 1

    return player_cards
