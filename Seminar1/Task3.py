# В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?
import math

def calculate_probability():
    total_parts = 15
    painted_parts = 9
    selected_parts = 3

    # Calculate the total number of possible combinations
    total_combinations = math.comb(total_parts, selected_parts)

    # Calculate the number of successful outcomes
    success_combinations = math.comb(painted_parts, selected_parts)
    probability = success_combinations / total_combinations
    return probability

# Main program
print("Calculating the probability that all extracted parts are painted...")
prob_all_painted = calculate_probability()
print(f"Probability: {prob_all_painted}")
