# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
import numpy as np
from scipy.stats import wilcoxon

def perform_paired_wilcoxon(data1, data2):
    statistic, p_value = wilcoxon(data1, data2)
    if p_value < alpha:
        print("Reject the null hypothesis. There are statistically significant differences.")
    else:
        print("Fail to reject the null hypothesis. There are no statistically significant differences.")

# Given data
data1 = np.array([150, 160, 165, 145, 155])
data2 = np.array([140, 155, 150, 130, 135])
alpha = 0.05

# Perform the paired t-test
perform_paired_wilcoxon(data1, data2)
