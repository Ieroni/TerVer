# В университет на факультеты A и B поступило равное количество студентов,
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9.
# Студент сдал первую сессию. Какова вероятность, что он учится:
# a). на факультете A б). на факультете B в). на факультете C?
p_a_pass = 0.8
p_b_pass = 0.7
p_c_pass = 0.9
p_a = 1 / 3  # Probability of being in faculty A
p_b = 1 / 3  # Probability of being in faculty B
p_c = 1 / 3  # Probability of being in faculty C

def calculate_probability_faculty_a():
    # Calculate the probability of passing the first session
    p_pass = p_a * p_a_pass + p_b * p_b_pass + p_c * p_c_pass
    # Calculate the probability of being in faculty A given that the student passed
    probability = (p_a * p_a_pass) / p_pass
    return probability

def calculate_probability_faculty_b():
    # Calculate the probability of passing the first session
    p_pass = p_a * p_a_pass + p_b * p_b_pass + p_c * p_c_pass
    # Calculate the probability of being in faculty B given that the student passed
    probability = (p_b * p_b_pass) / p_pass
    return probability

def calculate_probability_faculty_c():
    # Calculate the probability of passing the first session
    p_pass = p_a * p_a_pass + p_b * p_b_pass + p_c * p_c_pass
    # Calculate the probability of being in faculty C given that the student passed
    probability = (p_c * p_c_pass) / p_pass
    return probability

# Main program
print("Calculating the probability that the student learns in faculty A...")
prob_faculty_a = calculate_probability_faculty_a()
print(f"Probability: {prob_faculty_a}")

print("\nCalculating the probability that the student learns in faculty B...")
prob_faculty_b = calculate_probability_faculty_b()
print(f"Probability: {prob_faculty_b}")

print("\nCalculating the probability that the student learns in faculty C...")
prob_faculty_c = calculate_probability_faculty_c()
print(f"Probability: {prob_faculty_c}")
