# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a
# ). первым спортсменом б). вторым спортсменом в). третьим спортсменом.
p_first = 0.9
p_second = 0.8
p_third = 0.6

def calculate_probability_first_athlete():
    total_prob = p_first + p_second + p_third
    probability = p_first / total_prob
    return probability

def calculate_probability_second_athlete():
    total_prob = p_first + p_second + p_third
    probability = p_second / total_prob
    return probability

def calculate_probability_third_athlete():
    total_prob = p_first + p_second + p_third
    probability = p_third / total_prob
    return probability

# Main program
print("Calculating the probability that the shot was fired by the first athlete...")
prob_first_athlete = calculate_probability_first_athlete()
print(f"Probability: {prob_first_athlete}")

print("\nCalculating the probability that the shot was fired by the second athlete...")
prob_second_athlete = calculate_probability_second_athlete()
print(f"Probability: {prob_second_athlete}")

print("\nCalculating the probability that the shot was fired by the third athlete...")
prob_third_athlete = calculate_probability_third_athlete()
print(f"Probability: {prob_third_athlete}")
