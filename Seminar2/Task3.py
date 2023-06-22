# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

import math

def calculate_probability():
    total_attempts = 144
    selected_att = 70
    regular_prob = 0.5

    # Calculate the total number of possible combinations
    total_combinations = math.comb(total_attempts, selected_att)
    # Calculate the number of successful outcomes
    probability =total_combinations*(regular_prob**selected_att)*regular_prob**(total_attempts-selected_att)
    return probability

# Main program
print(f"Probability: {calculate_probability()}")