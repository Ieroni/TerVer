# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см,
# от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?
import math

def calculate_sigmas(observed_value, mean, standard_deviation):
    z_score = (observed_value - mean) / standard_deviation
    return z_score

# Given information
observed_value = 190
mean = 178
variance = 25
standard_deviation = math.sqrt(variance)

# Calculate the number of sigmas
sigmas = calculate_sigmas(observed_value, mean, standard_deviation)

# Print the result
print(f"The height of 190 cm deviates from the mean by {sigmas} standard deviations.")
