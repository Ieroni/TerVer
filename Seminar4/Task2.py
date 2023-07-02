# О случайной непрерывной равномерно распределенной величине B известно,
# что ее дисперсия равна 0.2. Можно ли найти правую границу величины B и ее среднее значение зная,
# что левая граница равна 0.5? Если да, найдите ее.
def calculate_right_boundary(variance, left_margin):
    # Variance of a uniform distribution: (b - a) ** 2 / 12
    right_boundary = (12 * variance) ** 0.5 + left_margin
    return right_boundary

def calculate_mean(left_margin, right_boundary):
    # Mean of a uniform distribution: (a + b) / 2
    mean = (left_margin + right_boundary) / 2
    return mean

# Given information
variance = 0.2
left_margin = 0.5

# Calculate right boundary and mean
right_boundary = calculate_right_boundary(variance, left_margin)
mean = calculate_mean(left_margin, right_boundary)

# Print the results
print(f"Right boundary: {right_boundary}")
print(f"Mean value: {mean}")
