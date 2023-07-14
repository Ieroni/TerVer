# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей
import numpy as np

def calculate_confidence_interval(data1, data2, confidence_level):
    sample_mean1 = np.mean(data1)
    sample_mean2 = np.mean(data2)
    sample_std1 = np.std(data1, ddof=1)  # ddof=1 for unbiased standard deviation
    sample_std2 = np.std(data2, ddof=1)  # ddof=1 for unbiased standard deviation
    sample_size1 = len(data1)
    sample_size2 = len(data2)
    margin_of_error = 1.96 * np.sqrt((sample_std1 ** 2 / sample_size1) + (sample_std2 ** 2 / sample_size2))  # 1.96 for 95% confidence level
    lower_bound = (sample_mean1 - sample_mean2) - margin_of_error
    upper_bound = (sample_mean1 - sample_mean2) + margin_of_error
    return lower_bound, upper_bound


# Given data for the heights of daughters and mothers
heights_daughters = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
heights_mothers = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
confidence_level = 0.95

# Calculate the confidence interval for the difference in heights
lower_bound, upper_bound = calculate_confidence_interval(heights_daughters, heights_mothers, confidence_level)

# Print the confidence interval for the difference in heights
print(f"The confidence interval for the difference in heights is [{lower_bound}, {upper_bound}]")
