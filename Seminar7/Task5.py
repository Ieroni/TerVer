# без функций для проведения тестов вручную.
# Выбрать тест и проверить, есть  ли различия между выборками. З
# аявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения.
# Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

import numpy as np

# Given data
data = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
hypothesized_mean = 2.5
alpha = 0.05
sample_size = len(data)

# Calculate the sample mean and standard deviation
sample_mean = np.mean(data)
sample_std = np.std(data, ddof=1)  # ddof=1 for unbiased standard deviation

# Calculate the t-statistic
t_statistic = (sample_mean - hypothesized_mean) / (sample_std / np.sqrt(sample_size))

# Calculate the degrees of freedom
degrees_of_freedom = sample_size - 1

# Calculate the critical t-value for a two-tailed test
critical_t = np.abs(t.ppf(alpha / 2, degrees_of_freedom))

# Compare the t-statistic with the critical t-value
if np.abs(t_statistic) > critical_t:
    print("Reject the null hypothesis. There are statistically significant differences.")
else:
    print("Fail to reject the null hypothesis. There are no statistically significant differences.")
