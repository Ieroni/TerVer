# В результате 10 независимых измерений некоторой величины X,
# выполненных с одинаковой точностью, получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала, покрывающего это значение
# с доверительной вероятностью 0,95. 3.Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей

import numpy as np
from scipy.stats import t

def calculate_confidence_interval(data, confidence_level):
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)  # ddof=1 for unbiased standard deviation
    sample_size = len(data)
    critical_t = t.ppf(1 - (1 - confidence_level) / 2, sample_size - 1)
    margin_of_error = critical_t * sample_std / np.sqrt(sample_size)
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound


# Given data for the value X
data_X = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
confidence_level_X = 0.95

# Calculate the confidence interval for value X
lower_X, upper_X = calculate_confidence_interval(data_X, confidence_level_X)

# Given data for the heights of daughters and mothers
heights_daughters = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
heights_mothers = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
confidence_level_heights = 0.95

# Calculate the difference in heights
heights_difference = np.array(heights_daughters) - np.array(heights_mothers)

# Calculate the confidence interval for the difference in heights
lower_heights, upper_heights = calculate_confidence_interval(heights_difference, confidence_level_heights)

# Print the confidence intervals
print(f"The confidence interval for the value X is [{lower_X}, {upper_X}]")
print(f"The confidence interval for the difference in heights is [{lower_heights}, {upper_heights}]")
