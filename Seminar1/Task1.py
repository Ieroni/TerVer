# Из колоды в 52 карты (n) извлекаются случайным образом 4 карты (k).
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
import math
import random
n = 0
k = 0

def combination (n,k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

# all combination
all_combinations = combination(52,4)
print(f"all possible combinations: {all_combinations}")

# ========== task A ================
# elements = 4 from submn = 13
kresti = combination(13,4)
print(f"kresti combinations: {kresti}")

# elements without = 39 and elems = 0; so comb2 = 1;
#  success combination  = Krest * 1
succs_combinationA = kresti
print(f"success combinations A: {succs_combinationA}")

# probability A
ProbabilityA = succs_combinationA/all_combinations
print(f"Probability A : {ProbabilityA}")

# =========== Task B ===========
# elements = 1 from submn = 4
Tuz = combination(4,1)
print(f"Tuz combinations: {Tuz}")

# elements without = 48 and elems = 3
neTuz = combination(48,3)
print(f"neTuz combinations: {neTuz}")

# Combination
succs_combinationB = Tuz*neTuz
print(f"success combinations B: {succs_combinationB}")

# probability B
ProbabilityB = succs_combinationB/all_combinations
print(f"Probability B: {ProbabilityB}")
