# Даны значения величины заработной платы заемщиков банка (zp)
# и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий,
# а затем с помощью функции cov из numpy Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.
import numpy as np
import pandas as pd

# Given data
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Calculate covariance using elementary operations
mean_zp = np.mean(zp)
mean_ks = np.mean(ks)
cov_e = np.sum((zp - mean_zp) * (ks - mean_ks)) / (len(zp) - 1)

# Calculate covariance using the cov function from numpy
cov_np = np.cov(zp, ks, ddof=1)[0, 1]

# Calculate Pearson correlation coefficient using elementary operations
std_zp = np.std(zp, ddof=1)
std_ks = np.std(ks, ddof=1)
corr_e = cov_e / (std_zp * std_ks)

# Calculate Pearson correlation coefficient using the corrcoef function from numpy
corr_np = np.corrcoef(zp, ks)[0, 1]

# Calculate Pearson correlation coefficient using the corr function from pandas
corr_pd = pd.DataFrame({'zp': zp, 'ks': ks}).corr().iloc[0, 1]

print("Covariance (Elementary):", cov_e)
print("Covariance (NumPy):", cov_np)
print("Pearson correlation coefficient (Elementary):", corr_e)
print("Pearson correlation coefficient (NumPy):", corr_np)
print("Pearson correlation coefficient (Pandas):", corr_pd)
