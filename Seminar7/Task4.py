# Даны 3 группы  учеников плавания.
# В 1 группе время на дистанцию 50 м составляют:
# 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54

import numpy as np
from scipy.stats import f_oneway

def perform_one_way_anova(data):
    statistic, p_value = f_oneway(*data)
    if p_value < alpha:
        print("Reject the null hypothesis. There are statistically significant differences among the groups.")
    else:
        print("Fail to reject the null hypothesis. There are no statistically significant differences among the groups.")

# Given data for the three groups
group1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
group2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
group3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
alpha = 0.05

# Perform the one-way ANOVA test
perform_one_way_anova([group1, group2, group3])
