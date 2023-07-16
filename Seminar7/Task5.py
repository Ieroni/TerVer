# без функций для проведения тестов вручную.
# Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения.
# Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
import numpy as np
from scipy.stats import t

def perform_two_sided_t_test(sample, hypothesized_mean, alpha):
    sample_size = len(sample)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)  # ddof=1 for unbiased standard deviation

    # Calculate the t-score
    t_score = (sample_mean - hypothesized_mean) / (sample_std / np.sqrt(sample_size))

    # Calculate the critical t-value
    df = sample_size - 1
    critical_t = t.ppf(alpha / 2, df)

    # Perform the two-sided test
    if np.abs(t_score) > critical_t:
        # Reject the null hypothesis
        print("Reject the null hypothesis.")
    else:
        # Fail to reject the null hypothesis
        print("Fail to reject the null hypothesis.")


# Given information
sample = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
hypothesized_mean = 2.5
alpha = 0.05
# Perform the two-sided t-test
perform_two_sided_t_test(sample, hypothesized_mean, alpha)