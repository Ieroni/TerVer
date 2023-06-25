# В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?
from math import comb

total_balls_box1 = 8
white_balls_box1 = 5
total_balls_box2 = 12
white_balls_box2 = 5
draw_balls_box1 = 2
draw_balls_box2 = 4

def calculate_probability_three_white():
    # Calculate the probability of drawing 3 white balls
    total_ways = comb(total_balls_box1, draw_balls_box1) * comb(total_balls_box2, draw_balls_box2)
    ways_white_3 = comb(white_balls_box1, 2) * comb(white_balls_box2, 1) + comb(white_balls_box1, 1) * comb(
        white_balls_box2, 2)
    probability = ways_white_3 / total_ways
    return probability

# Main program
print("Calculating the probability that 3 balls drawn are white...")
prob_three_white = calculate_probability_three_white()
print(f"Probability: {prob_three_white}")
