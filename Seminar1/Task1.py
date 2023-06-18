# Из колоды в 52 карты извлекаются случайным образом 4карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди4-х карт окажется хотя бы один туз.

import random

def draw_cards():
    deck = ['Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs',
            '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs',
            'King of Clubs', 'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds',
            '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds',
            '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Hearts',
            '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts',
            '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',
            'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades',
            '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades',
            'King of Spades']

    # Randomly select 4 cards from the deck
    drawn_cards = random.sample(deck, 4)

    return drawn_cards

def probability_all_clubs():
    total_trials = 100000  # Number of trials to run
    success_count = 0  # Count of trials where all cards are clubs

    for _ in range(total_trials):
        drawn_cards = draw_cards()
        if all('Clubs' in card for card in drawn_cards):
            success_count += 1

    probability = success_count / total_trials
    return probability


def probability_at_least_one_ace():
    total_trials = 100000  # Number of trials to run
    success_count = 0  # Count of trials where at least one ace is drawn

    for _ in range(total_trials):
        drawn_cards = draw_cards()
        if any('Ace' in card for card in drawn_cards):
            success_count += 1

    probability = success_count / total_trials
    return probability


# Main program
print("Calculating probability that all cards are clubs...")
prob_clubs = probability_all_clubs()
print(f"Probability: {prob_clubs}")

print("\nCalculating probability of at least one ace...")
prob_ace = probability_at_least_one_ace()
print(f"Probability: {prob_ace}")
