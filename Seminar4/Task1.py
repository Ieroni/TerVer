# Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.
def calculate_mean():
    lower_bound = 200
    upper_bound = 800

    # Mean of a uniform distribution
    mean = (lower_bound + upper_bound) / 2
    return mean

def calculate_variance():
    lower_bound = 200
    upper_bound = 800

    # Variance of a uniform distribution
    variance = ((upper_bound - lower_bound) ** 2) / 12
    return variance

# Main program
print("Calculating the mean of the uniform distribution...")
mean = calculate_mean()
print(f"Mean: {mean}")

print("\nCalculating the variance of the uniform distribution...")
variance = calculate_variance()
print(f"Variance: {variance}")
