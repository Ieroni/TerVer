# Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)
import math

def calculate_mean():
    mean = -2  # Mean of the normal distribution
    return mean

def calculate_variance():
    variance = 32  # Variance of the normal distribution
    return variance

def calculate_standard_deviation(variance):
    standard_deviation = math.sqrt(variance)  # Standard deviation is the square root of variance
    return standard_deviation

# Main program
print("Calculating the mean (M(X)) of the normal distribution...")
mean = calculate_mean()
print(f"Mean: {mean}")

print("\nCalculating the variance (D(X)) of the normal distribution...")
variance = calculate_variance()
print(f"Variance: {variance}")

print("\nCalculating the standard deviation (std(X)) of the normal distribution...")
standard_deviation = calculate_standard_deviation(variance)
print(f"Standard Deviation: {standard_deviation}")
