# Исследовалось влияние препарата на уровень давления пациентов.
# Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут.
# Есть ли статистически значимые различия?
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150,  130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125

import numpy as np
from scipy.stats import friedmanchisquare

def perform_repeated_measures_friedmanchisquare(data):
    statistic, p_value = friedmanchisquare(*data)
    if p_value < alpha:
        print("Reject the null hypothesis. There are statistically significant differences.")
    else:
        print("Fail to reject the null hypothesis. There are no statistically significant differences.")

# Given data
data = np.array([[150, 160, 165, 145, 155],
                 [140, 155, 150, 130, 135],
                 [130, 130, 120, 130, 125]])
alpha = 0.05

# Perform the repeated measures kruskal test
perform_repeated_measures_friedmanchisquare(data)
