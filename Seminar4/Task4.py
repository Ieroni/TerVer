# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.
import scipy.stats as stats

def calculate_probability_above(value, mean, std_dev):
    z_score = (value - mean) / std_dev
    probability = 1 - stats.norm.cdf(z_score)
    return probability


def calculate_probability_between(lower, upper, mean, std_dev):
    z_lower = (lower - mean) / std_dev
    z_upper = (upper - mean) / std_dev
    probability = stats.norm.cdf(z_upper) - stats.norm.cdf(z_lower)
    return probability


def calculate_probability_below(value, mean, std_dev):
    z_score = (value - mean) / std_dev
    probability = stats.norm.cdf(z_score)
    return probability


# Given information
mean = 174
std_dev = 8

# Calculate probabilities
probability_a = calculate_probability_above(182, mean, std_dev)
probability_b = calculate_probability_above(190, mean, std_dev)
probability_c = calculate_probability_between(166, 190, mean, std_dev)
probability_d = calculate_probability_between(166, 182, mean, std_dev)
probability_e = calculate_probability_between(158, 190, mean, std_dev)
probability_f = 1 - (stats.norm.cdf(150, mean, std_dev) - stats.norm.cdf(190, mean, std_dev))
probability_g = 1 - (stats.norm.cdf(150, mean, std_dev) - stats.norm.cdf(198, mean, std_dev))
probability_h = calculate_probability_below(166, mean, std_dev)

# Print the results
print(f"Probability of height over 182 cm: {probability_a}")
print(f"Probability of height over 190 cm: {probability_b}")
print(f"Probability of height from 166 cm to 190 cm: {probability_c}")
print(f"Probability of height from 166 cm to 182 cm: {probability_d}")
print(f"Probability of height from 158 cm to 190 cm: {probability_e}")
print(f"Probability of height not higher than 150 cm or not lower than 190 cm: {probability_f}")
print(f"Probability of height not higher than 150 cm or not lower than 198 cm: {probability_g}")
print(f"Probability of height below 166 cm: {probability_h}")
