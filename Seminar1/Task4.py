# В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
import math

def calculate_probability():
    total_tickets = 100
    winning_tickets = 2
    selected_tickets = 2

    # Calculate the total number of possible combinations
    total_combinations = math.comb(total_tickets, selected_tickets)

    # Calculate the number of successful outcomes
    success_combinations = math.comb(winning_tickets, selected_tickets)
    probability = success_combinations / total_combinations
    return probability

# Main program
print("Calculating the probability that two purchased tickets will be winning...")
prob_both_winning = calculate_probability()
print(f"Probability: {prob_both_winning}")
