# Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением,
# равным 16. Найти доверительный интервал для оценки математического ожидания a с надежностью
# \0.95, если выборочная средняя M = 80, а объем выборки n = 256.
import numpy as np
import scipy.stats as stats

def calculate_confidence_interval(sample_mean, sample_size, population_std, reliability):
    # Calculate the critical z-value
    alpha = 1 - reliability
    critical_z = stats.norm.ppf(1 - alpha / 2)

    # Calculate the standard error
    standard_error = population_std / np.sqrt(sample_size)

    # Calculate the margin of error
    margin_of_error = critical_z * standard_error

    # Calculate the lower and upper bounds of the confidence interval
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error

    return lower_bound, upper_bound


# Given information
sample_mean = 80
sample_size = 256
population_std = 16
reliability = 0.95

# Calculate the confidence interval
lower, upper = calculate_confidence_interval(sample_mean, sample_size, population_std, reliability)

# Print the confidence interval
print(f"The confidence interval for the population mean is [{lower}, {upper}]")
