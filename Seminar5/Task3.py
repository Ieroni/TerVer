# Проведите тест гипотезы. Продавец утверждает,
# что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек.
# Вес каждой пачки составляет: 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально. Верно ли утверждение продавца, если учитывать,
# что доверительная вероятность равна 99%? (Провести двусторонний тест.)
import numpy as np
from scipy.stats import t

def perform_two_sided_t_test(sample, population_mean, confidence_level):
    sample_size = len(sample)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)  # ddof=1 for unbiased standard deviation

    # Calculate the t-score
    t_score = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))

    # Calculate the critical t-value
    alpha = 1 - confidence_level
    df = sample_size - 1
    critical_t = t.ppf(alpha / 2, df)

    # Perform the two-sided test
    if np.abs(t_score) > critical_t:
        # Reject the null hypothesis
        print("Reject the null hypothesis")
    else:
        # Fail to reject the null hypothesis
        print("Fail to reject the null hypothesis")


# Given information
sample = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
population_mean = 200
confidence_level = 0.99

# Perform the two-sided t-test
perform_two_sided_t_test(sample, population_mean, confidence_level)
