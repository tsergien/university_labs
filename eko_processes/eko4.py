#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit , minimize

p = 10
w1 = 2
w2 = 3
TC = 170_000
q0 = 148_000

df = pd.DataFrame({
    'K':[5700,  4840, 4590, 5330, 5200, 4160, 5000, 4690, 5890, 4930],
    'L':[14245, 13340, 13860, 14400, 14000, 12000, 14145, 13900, 15050, 13060],
    'Q':[140330, 122355, 123000, 137330, 121570, 113100, 131000, 124165, 149000, 120950]
})

print(df[['K', 'L']])

a, A = curve_fit(lambda kl, a, A: A * kl['K']**a * kl['L']**(1-a), df[['K', 'L']], df['Q'])[0]
print("a = ", a)
print("A = ", A)

# cl[0] - K, cl[1] - L

def production(cl):
    return A * cl[0]**a * cl[1]**(1-a)

def costs(cl):
    return w1 * cl[0] + w2 * cl[1]

def profit(cl):
    return p * production(cl) - costs(cl)

def minus_profit(cl):
    return - profit(cl)


cl_star_1 = minimize(
    minus_profit,
    x0=(10_000, 10_000),
    constraints=(
    {'type': 'ineq', 'fun': lambda cl: costs(cl)},
    {'type': 'ineq', 'fun': lambda cl: TC - costs(cl)},
    )
    )['x']
print(
    'limited cost, maximal profit:\n'
    f' cl_star = {cl_star_1}\n'
    f' costs(cl_star) = {costs(cl_star_1)}\n'
    f' product(cl_star) = {production(cl_star_1)}\n'
    f' profit(cl_star) = {profit(cl_star_1)}\n'
    )