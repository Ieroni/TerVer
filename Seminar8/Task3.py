# Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности,
# равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
import numpy as np
from scipy.stats import t

# Given data
sample_size = 27
sample_mean = 174.2
population_variance = 25
alpha = 0.05

# Calculate the standard deviation of the population
population_std = np.sqrt(population_variance)

# Calculate the critical t-value for the confidence interval
degrees_of_freedom = sample_size - 1
critical_t = t.ppf(1 - alpha/2, degrees_of_freedom)

# Calculate the margin of error
margin_of_error = critical_t * population_std / np.sqrt(sample_size)

# Calculate the confidence interval
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print("Confidence Interval:", confidence_interval)
