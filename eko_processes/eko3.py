#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit, root_scalar

df = pd.DataFrame({
    'price':[1.3,  2.5, 2.8, 3.5, 4.7, 5.6, 6.3, 7.2],
    'demand':[103, 82,  67,  53,  44,  36,  27,  15],
    'supply':[10,  29,  38,  48,  60,  83,  91,  106]
})
print(df)

p_l, p_r, q_l, q_r = 1, 6, 10, 130


class SupplyLin(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a * t + b, 
			df['price'], df['supply'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a * t + self.b

	def __repr__(self):
		return f'{self.a:.2f} * t + {self.b:.2f}'


class DemandExp(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a * np.exp(b * t), 
			df['price'], df['demand'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a * np.exp(self.b * t)

	def __repr__(self):
		return f'{self.a:.2f} * exp({self.b:.2f} * t)'


f = {'supply_lin': SupplyLin(df), 'demand_exp': DemandExp(df)}

price_space = np.arange(1, 6, .01)

df_interp = pd.DataFrame({
	'price': price_space,
	'demand': f['demand_exp'](price_space),
	'supply': f['supply_lin'](price_space),
})

p = root_scalar(lambda t: f['demand_exp'](t) - f['supply_lin'](t), x0=p_l, x1=p_r).root
q = (f['demand_exp'](p) + f['supply_lin'](p)) / 2


plt.figure(figsize=(20,20))
plt.scatter(df['demand'], df['price'], s=100, 
	marker='x', c='k', label='$Q_d(P)$, true')
plt.scatter(df['supply'], df['price'], s=100, 
	marker='x', c='b', alpha=.5, label='$Q_s(P)$, true')
plt.plot(df_interp['supply'], df_interp['price'], 
	'b-', alpha=.5, label='$Q_s(P)$', zorder=1)
plt.plot(df_interp['demand'], df_interp['price'], 
	'k-', label='$Q_d(P)$', zorder=1)
plt.scatter(q, p, s=100, c='k', label=f'({q:.2f}, {p:.2f})', zorder=2)
plt.axvline(q, 0, (p - p_l) / (p_r - p_l), c='k', linestyle='--')
plt.axhline(p, 0, (q - q_l) / (q_r - q_l), c='k', linestyle='--')
plt.title(' $(Q, P)$', fontsize=20)
plt.xlabel('$Q$', fontsize=16)
plt.ylabel('$P$', fontsize=16)
plt.xlim((q_l, q_r))
plt.ylim((p_l, p_r))
plt.legend(loc='right', fontsize=16)
plt.grid(True)
plt.show()

subsidy = 0.2

df_dot = pd.DataFrame({
	'price': price_space,
	'demand': f['demand_exp'](price_space - subsidy),
	'supply': f['supply_lin'](price_space),
})

p = root_scalar(lambda t: f['demand_exp'](t - subsidy) - f['supply_lin'](t), 
	x0=p_l, x1=p_r).root
q = (f['demand_exp'](p - subsidy) + f['supply_lin'](p)) / 2


plt.figure(figsize=(20,20))
plt.plot(df_dot['supply'], df_dot['price'], 
	'b-', alpha=.5, label='$Q_s(P)$', zorder=1)
plt.plot(df_dot['demand'], df_dot['price'], 
	'k-', label='$Q_d^{sub}(P)$', zorder=1)
plt.plot(df_interp['demand'], df_interp['price'], 
	'k--', label='$Q_d(P)$', zorder=1)
plt.scatter(q, p, s=100, c='k', label=f'({q:.2f}, {p:.2f})', zorder=2)
plt.axvline(q, 0, (p - p_l) / (p_r - p_l), c='k', linestyle='--')
plt.axhline(p, 0, (q - q_l) / (q_r - q_l), c='k', linestyle='--')
plt.title(f'$subsidy={subsidy}$', fontsize=20)
plt.xlabel('$Q$', fontsize=16)
plt.ylabel('$P$', fontsize=16)
plt.xlim((q_l, q_r))
plt.ylim((p_l, p_r))
plt.legend(loc='right', fontsize=16)
plt.grid(True)
plt.show()
