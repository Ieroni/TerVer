# Даны две  независимые выборки. Не соблюдается условие нормальности
# x1  380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции

import numpy as np
from scipy.stats import mannwhitneyu

def perform_mannwhitneyu_test(x, y, alpha):
    statistic, p_value = mannwhitneyu(x, y, alternative='two-sided')
    if p_value < alpha:
        print("Reject the null hypothesis. There is a statistically significant difference between the two samples.")
    else:
        print("Fail to reject the null hypothesis. There is no statistically significant difference between the two samples.")

# Given data
x1 = np.array([380.420, 290])
y1 = np.array([140, 360, 200, 900])
alpha = 0.05

# Perform the Mann-Whitney U test
perform_mannwhitneyu_test(x1, y1, alpha)
