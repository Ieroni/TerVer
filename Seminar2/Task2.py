# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день?
# Какова вероятность, что перегорят ровно две?

import math
def combination (m,n,p):
    lmbd = p * n
    e = 2.72
    return (lmbd**m//math.factorial(m))*e**(-lmbd)
ProbabilityA = combination(0,5000,0.0004)
ProbabilityB = combination(2,5000,0.0004)
print(f"all possible combinations: {ProbabilityA}")
print(f"all possible combinations: {ProbabilityB}")