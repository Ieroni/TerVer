# В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?
import math

def calculate_probability_all_white():
    total_outcomes = math.comb(10, 2) * math.comb(11, 2)
    success_outcomes = math.comb(7, 2) * math.comb(9, 2)
    probability = success_outcomes / total_outcomes
    return probability

def calculate_probability_exactly_two_white():
    total_outcomes = math.comb(10, 2) * math.comb(11, 2)
    success_outcomes = (math.comb(7, 2) * math.comb(2, 0)) * (math.comb(9, 2) * math.comb(2, 0))
    probability = success_outcomes / total_outcomes
    return probability

def calculate_probability_at_least_one_white():
    total_outcomes = math.comb(10, 2) * math.comb(11, 2)
    success_outcomes = (math.comb(7, 2) * math.comb(3, 0)) * (math.comb(9, 2) * math.comb(2, 0)) + \
                       (math.comb(7, 1) * math.comb(3, 1)) * (math.comb(9, 1) * math.comb(2, 1)) + \
                       (math.comb(7, 0) * math.comb(3, 2)) * (math.comb(9, 0) * math.comb(2, 2))
    probability = success_outcomes / total_outcomes
    return probability

# Main program
print("Calculating the probability that all balls are white...")
prob_all_white = calculate_probability_all_white()
print(f"Probability: {prob_all_white}")

print("\nCalculating the probability that exactly two balls are white...")
prob_two_white = calculate_probability_exactly_two_white()
print(f"Probability: {prob_two_white}")

print("\nCalculating the probability that at least one ball is white...")
prob_at_least_one_white = calculate_probability_at_least_one_white()
print(f"Probability: {prob_at_least_one_white}")
