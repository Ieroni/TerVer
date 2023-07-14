# В результате 10 независимых измерений некоторой величины X,
# выполненных с одинаковой точностью, получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала, покрывающего это значение
# с доверительной вероятностью 0,95.
import numpy as np

def calculate_confidence_interval(data, confidence_level):
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)  # ddof=1 for unbiased standard deviation
    sample_size = len(data)
    margin_of_error = 1.96 * sample_std / np.sqrt(sample_size)  # 1.96 for 95% confidence level
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound


# Given data for the value X
data_X = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
confidence_level_X = 0.95

# Calculate the confidence interval for value X
lower_X, upper_X = calculate_confidence_interval(data_X, confidence_level_X)

# Print the confidence interval for value X
print(f"The confidence interval for the value X is [{lower_X}, {upper_X}]")
