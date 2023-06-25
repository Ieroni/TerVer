# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.
import math

def calculate_arithmetic_mean(data):
    total = sum(data)
    mean = total / len(data)
    return mean

def calculate_standard_deviation(data, biased=True):
    mean = calculate_arithmetic_mean(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data) if biased else sum(squared_diff) / (len(data) - 1)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

def calculate_biased_variance(data):
    return calculate_standard_deviation(data, biased=True) ** 2

def calculate_unbiased_variance(data):
    return calculate_standard_deviation(data, biased=False) ** 2

# Main program
sample_data = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
mean = calculate_arithmetic_mean(sample_data)
print(f"Arithmetic Mean: {mean}")

std_dev = calculate_standard_deviation(sample_data)
print(f"Standard Deviation (biased): {std_dev}")

biased_var = calculate_biased_variance(sample_data)
print(f"Biased Variance: {biased_var}")

unbiased_var = calculate_unbiased_variance(sample_data)
print(f"Unbiased Variance: {unbiased_var}")
