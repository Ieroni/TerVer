# Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
import numpy as np
from scipy.stats import t

# Given data
iq_values = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
sample_size = len(iq_values)
alpha = 0.05

# Calculate the sample mean and standard deviation
sample_mean = np.mean(iq_values)
sample_std = np.std(iq_values, ddof=1)  # ddof=1 for unbiased standard deviation

# Calculate the critical t-value for the confidence interval
degrees_of_freedom = sample_size - 1
critical_t = t.ppf(1 - alpha/2, degrees_of_freedom)

# Calculate the margin of error
margin_of_error = critical_t * sample_std / np.sqrt(sample_size)

# Calculate the confidence interval
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print("Confidence Interval:", confidence_interval)
