# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
import itertools

def calculate_probability():
    total_combinations = 10 * 9 * 8  # Total number of possible combinations

    # Generate all possible combinations of 3 numbers from 0 to 9
    combinations = list(itertools.combinations(range(10), 3))

    success_count = len(combinations)  # Count of successful outcomes

    probability = success_count / total_combinations
    return probability


# Main program
print("Calculating the probability of opening the door on the first try...")
prob_first_try = calculate_probability()
print(f"Probability: {prob_first_try}")
