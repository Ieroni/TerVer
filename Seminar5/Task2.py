# Проведите тест гипотезы. Утверждается, что шарики для подшипников,
# изготовленные автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0,05, проверить эту гипотезу,
# если в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм,
# а дисперсия известна и равна 4 кв. мм.
import numpy as np
from scipy.stats import norm

def perform_one_tailed_z_test(sample_mean, population_mean, population_variance, sample_size, alpha):
    # Calculate the standard deviation (standard error)
    standard_deviation = np.sqrt(population_variance / sample_size)

    # Calculate the z-score
    z_score = (sample_mean - population_mean) / standard_deviation

    # Calculate the critical z-value
    critical_z = norm.ppf(1 - alpha)

    # Perform the one-tailed test
    if z_score > critical_z:
        # Reject the null hypothesis
        print("Reject the null hypothesis")
    else:
        # Fail to reject the null hypothesis
        print("Fail to reject the null hypothesis")


# Given information
sample_mean = 17.5
population_mean = 17
population_variance = 4
sample_size = 100
alpha = 0.05

# Perform the one-tailed z-test
perform_one_tailed_z_test(sample_mean, population_mean, population_variance, sample_size, alpha)
