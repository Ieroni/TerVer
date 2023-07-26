# Провести дисперсионный анализ для определения того,
# есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
import scipy.stats as sts
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

# Given data
football_players = np.array([173, 175, 180, 178, 177, 185, 183, 182,])
hockey_players = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

# Mean's calculating
y_mean_footballers = np.mean(football_players)
y_mean_hockeyers = np.mean(hockey_players)
y_mean_weightlifters = np.mean(weightlifters)
print(f'footballers mean: {y_mean_footballers}')
print(f'hockey_players: {y_mean_hockeyers}')
print(f'weightlifters: {y_mean_weightlifters}')
print('=======================================')
#Normal checking
a = sts.shapiro(football_players)
b = sts.shapiro(hockey_players)
c = sts.shapiro(weightlifters)
print(f'{a} {b} {c}')
PvaluesList = [a.pvalue, b.pvalue, c.pvalue]
alpha = 0.05
NormalCheking = [True if p_value > alpha else False for p_value in PvaluesList]
print(PvaluesList)
print(f'normal cheking: {NormalCheking}')
print('=======================================')

#dispersian cheking
d = sts.bartlett(football_players, hockey_players, weightlifters)
DispersCheking = [True if d.pvalue > alpha else False]
print(f'{d}')
print(f'dispersion cheking: {DispersCheking}')
print('=======================================')

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(football_players, hockey_players, weightlifters)
print(f'{y_mean_footballers}  {y_mean_hockeyers} {y_mean_weightlifters}')
print("F-statistic:", f_statistic)
print("p-value:", p_value)
print('=======================================')

# Post hock test Tukey
#  для 1ого post hock testa пришлось добавит вручную данные около среднего арифметического
dataArray = [173, 175, 180, 178, 177, 185, 183, 182, 179.125, 179.125, 179.125,
             177, 179, 180, 188, 177, 172, 171, 184, 178.666, 178.666, 178.666,
             172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]
df = pd.DataFrame({'score': dataArray,
                   'group': np.repeat(['football_players', 'hockey_players', 'weightlifters'], repeats=11)})
tukey = pairwise_tukeyhsd(endog=df['score'],
                          groups=df['group'],
                          alpha=0.05)
print(tukey)

#  вызов функции сравнения по парам
print (sts.tukey_hsd(football_players,hockey_players,weightlifters))