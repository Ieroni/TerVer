# Задачу 4 решать с помощью функции. 4.
# Есть ли статистически значимые различия в росте дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160
import numpy as np
from scipy.stats import t

def perform_paired_t_test(mothers_height, daughters_height, alpha):
    # Convert the data to NumPy arrays
    mothers_height = np.array(mothers_height)
    daughters_height = np.array(daughters_height)

    # Calculate the differences between daughters' and mothers' heights
    differences = daughters_height - mothers_height

    # Calculate the sample size
    sample_size = len(differences)

    # Calculate the mean and standard deviation of the differences
    mean_diff = np.mean(differences)
    std_diff = np.std(differences, ddof=1)  # ddof=1 for unbiased standard deviation

    # Calculate the standard error
    se_diff = std_diff / np.sqrt(sample_size)

    # Calculate the t-score
    t_score = mean_diff / se_diff

    # Calculate the degrees of freedom
    df = sample_size - 1

    # Calculate the critical t-value
    critical_t = t.ppf(1 - alpha / 2, df)

    # Perform the two-tailed t-test
    if np.abs(t_score) > critical_t:
        # Reject the null hypothesis
        print("There are statistically significant differences in the height of daughters.")
    else:
        # Fail to reject the null hypothesis
        print("There are no statistically significant differences in the height of daughters.")


# Given data
mothers_height = [172, 177, 158, 170, 178, 175, 164, 160, 169]
daughters_height = [173, 175, 162, 174, 175, 168, 155, 170, 160]
alpha = 0.05

# Perform the paired t-test
perform_paired_t_test(mothers_height, daughters_height, alpha)
