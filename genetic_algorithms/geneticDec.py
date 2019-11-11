#!/usr/bin/python3

import math
import numpy as np
import random
from functools import reduce
from typing import Tuple
from itertools import accumulate 
import time

def rastrigin(x: np.array) -> float:
	return -10 * _m - np.sum(np.power(x, 2) - 10 * np.cos(2 * np.pi * x))

# -----> ackley function : x in [-5, 5]
def ackley(x: np.array) -> float:
    return -20 * math.exp(-0.2 * math.sqrt(x[0]**2 + x[1]**2)) - \
        math.exp(0.5 * ( math.cos(2*math.pi*x[0]) + math.cos(2*math.pi*x[1]) ) ) + \
            math.e + 20

# -----> rosenbroke function
def rosenbroke(x: np.array) -> float:
    r = 0
    for i in range(len(x) - 1):
        r += 100 * (x[i+1] - x[i]*x[i])**2 + (x[i] - 1)**2
    return r

def _cod_decimal(xbin: np.array, xmin: float, d: float) -> float:
	xdec1 = reduce(lambda _1, _2: _1 * 2 + _2, map(int, xbin[::-1]))
	return xmin + d * xdec1

def CodDecimal(rows: int, cols: int, g_bin: np.matrix, x_min: np.array, NN: np.array,
                    dd: np.array) -> np.matrix:
    _m: int = NN.shape[0] - 1
    return np.matrix([[
        _cod_decimal(np.asarray(g_bin[i, NN[j]:NN[j + 1]]).reshape(-1), x_min[j], dd[j])
    for j in range(_m)] for i in range(n)])

def _cod_binary(xdec: float, xmin: float, l: int, d: float) -> np.array:
	xx = int(np.floor((xdec - xmin) / d))
	digits = list(map(int, bin(xx)[:1:-1]))
	return np.array(digits + [0 for _ in range(l - len(digits))])

def CodBinary(n: int, m: int, g_dec: np.matrix, x_min: np.array,
                   nn: np.array, dd: np.array) -> np.matrix:
    return np.matrix([
        np.hstack([
            _cod_binary(g_dec[i, j], x_min[j], nn[j], dd[j]) for j in range(m)
        ]) for i in range(n)
    ])

def GenerationDec(rows: int, cols: int, x_min: np.array, x_max: np.array) -> np.matrix:
	return  np.random.uniform(low=x_min, high=x_max, size=(rows, cols))

def BinDecParam(rows: int, cols: int, x_min: np.array, x_max: np.array, 
					eps: float) -> Tuple[np.array, np.array, np.array]:    
	nn = (np.floor(np.log2((x_max - x_min) / eps)) + 1).astype(int)
	dd = np.round((x_max - x_min) / (np.power(2, nn) - 1), 7)
	NN = np.array([0,] + list(accumulate(nn)))
	return nn, dd, NN

def Parens(n: int):
	p = np.random.permutation(np.arange(n << 1))
	return p[:n], p[n:]

def Adapt(periodic: np.array) -> np.array:
	n : int = len(periodic)
	periodic -= np.min(periodic)
	periodic /= np.sum(periodic)
	num = np.zeros(n)
	for roll in np.random.choice(np.arange(n), n, p=periodic):
		num[roll] += 1
	return num.astype(int)

def Mutation(G: np.matrix, p: float) -> Tuple[np.matrix, int]:
	mask = np.random.uniform(size=G.shape) < p
	return G ^ mask, np.sum(np.sum(mask))

def Crossover(G: np.matrix, n: int, m_list: np.array, f_list: np.array):
	cros = np.random.randint(low=0, high=G.shape[1], size=n)
	g_cros = np.copy(G)
	for m, f, c in zip(m_list, f_list, cros):
		g_cros[[m, f], :c] = g_cros[[f, m], :c]
	return g_cros


def best(m: int, g_dec: np.matrix) -> int:
	return np.argmax(g_dec[:, m])

def worst(m: int, g_dec: np.matrix) -> int:
	return np.argmin(g_dec[:, m])


def new_generation(g_dec: np.matrix, num: np.array) -> np.matrix:
	return np.repeat(g_dec, repeats=num, axis=0)

#########################################################################
#########################################################################
#########################################################################
#########################################################################


np.set_printoptions(linewidth=100)
np.random.seed(65537)
n, _m = 1 << 10, 2
print(f'Population: {n}, dimension: {_m}')
p = 2e-2

x_min, x_max = np.repeat(-5.12, _m), np.repeat(5.12, _m)
# x_min, x_max = np.repeat(-5, _m), np.repeat(5, _m)
g_dec = GenerationDec(n, _m, x_min, x_max)
eps = 1e-5
nn, dd, NN = BinDecParam(n, _m, x_min, x_max, eps)

# print(
# 	f'nn = {nn}\n'
# 	f'dd = {dd}\n'
# 	f'NN = {NN}'
# )

t0 = time.time()
for _ in range(1, 1 << 12): # 12
	g_bin = CodBinary(n, _m, g_dec, x_min, nn, dd)

	g_bin, mutation_count = Mutation(g_bin, p)

	m, f = Parens(n >> 1)

	g_bin = Crossover(g_bin, n, m, f)

	g_dec = CodDecimal(n, _m, g_bin, x_min, NN, dd)

	f_vals = np.array([rastrigin(g_dec[i]) for i in range(n)]).reshape((n, 1))
	# f_vals = np.array([rosenbroke(g_dec[i]) for i in range(n)]).reshape((n, 1))
	# f_vals = np.array([ackley(g_dec[i]) for i in range(n)]).reshape((n, 1))

	if not (_ & 127):
		print(f'Iteration: {_}, max fitness function value: {np.max(f_vals)}')

	g_dec = np.hstack([g_dec, f_vals])

	b, w = best(_m, g_dec), worst(_m, g_dec)

	g_best = np.asarray(g_dec[b, :-1]).flatten()

	g_dec = np.delete(g_dec, w, axis=0)


	num = Adapt(np.asarray(g_dec[:, -1]).flatten())

	g_dec = np.vstack([new_generation(g_dec[:, :-1], num), g_best])


print(f'Generation: {g_dec}')
print(f'Time: {np.round(time.time() - t0)} seconds')

f_vals = np.array([rastrigin(g_dec[i]) for i in range(n)]).reshape((n, 1))

print(f'Best individual: {np.min(np.abs(f_vals))}')


