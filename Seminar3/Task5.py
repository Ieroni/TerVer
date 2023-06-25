# Устройство состоит из трех деталей.
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2,
# для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
p_fail_1 = 0.1
p_fail_2 = 0.2
p_fail_3 = 0.25

def calculate_probability_all_fail():
    probability = p_fail_1 * p_fail_2 * p_fail_3
    return probability

def calculate_probability_two_fail():
    # Probability of exactly two parts failing
    probability = (1 - p_fail_1) * p_fail_2 * p_fail_3 + p_fail_1 * (1 - p_fail_2) * p_fail_3 + p_fail_1 * p_fail_2 * (
                1 - p_fail_3)
    return probability

def calculate_probability_at_least_one_fail():
    # Probability of at least one part failing
    probability = 1 - (1 - p_fail_1) * (1 - p_fail_2) * (1 - p_fail_3)
    return probability

def calculate_probability_one_to_two_fail():
    # Probability of one or two parts failing
    probability = calculate_probability_at_least_one_fail() - calculate_probability_all_fail()
    return probability

# Main program
print("Calculating the probability that all three parts fail in the first month...")
prob_all_fail = calculate_probability_all_fail()
print(f"Probability: {prob_all_fail}")

print("\nCalculating the probability that exactly two parts fail in the first month...")
prob_two_fail = calculate_probability_two_fail()
print(f"Probability: {prob_two_fail}")

print("\nCalculating the probability that at least one part fails in the first month...")
prob_at_least_one_fail = calculate_probability_at_least_one_fail()
print(f"Probability: {prob_at_least_one_fail}")

print("\nCalculating the probability that from one to two parts fail in the first month...")
prob_one_to_two_fail = calculate_probability_one_to_two_fail()
print(f"Probability: {prob_one_to_two_fail}")