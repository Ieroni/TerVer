# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

import math
import random
p = 0.8
def combination (n,k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
all_combinations = combination(100,85)
print(f"all possible combinations: {all_combinations}")

Probability =all_combinations*(p**85)*((1-p)**15)
print(f"all possible combinations: {Probability}")