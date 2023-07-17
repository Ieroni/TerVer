# Даны значения величины заработной платы заемщиков банка (zp)
# и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии,
# приняв за X заработную плату (то есть, zp - признак),
# а за y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.
import numpy as np

# Given data
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Calculate the coefficients with intercept
n = len(zp)
X = np.vstack([zp, np.ones(n)]).T
coefficients_with_intercept = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(ks)

# Calculate the coefficients without intercept
X_without_intercept = zp.reshape(-1, 1)
coefficients_without_intercept = np.linalg.lstsq(X_without_intercept, ks, rcond=None)[0]

print("Coefficients with intercept:", coefficients_with_intercept)
print("Coefficients without intercept:", coefficients_without_intercept)
