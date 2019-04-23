#!/usr/bin/python3

import math
import numpy as np
import random
from functools import reduce
from typing import Tuple
from itertools import accumulate 


def CodDecimal(xbin: np.array, xmin: float, d: float):
	xdec1 = reduce(lambda _1, _2: _1 * 2 + _2, map(int, xbin[::-1]))
	return xmin + d * xdec1

def CodBinary(xdec: float, xmin: float, l: int, d: float) -> np.array:
	xx = int(np.floor((xdec - xmin) / d))
	digits = list(map(int, bin(xx)[:1:-1]))
	return np.array(digits + [0 for _ in range(l - len(digits))])

def GenerationDec(rows: int, cols: int, x_min: np.array, x_max: np.array) -> np.matrix:
	return  np.random.uniform(low=x_min, high=x_max, size=(rows, cols))

def BinDecParam(rows: int, cols: int, x_min: np.array, x_max: np.array, 
					eps: float) -> Tuple[np.array, np.array, np.array]:    
	nn = np.floor(np.log2((x_max - x_min) / eps)) + 1
	dd = np.round((x_max - x_min) / (np.power(2, nn) - 1), 7)
	NN = np.array([0,] + list(accumulate(nn)))
	return nn, dd, NN

def Parens(n: int):
	p = np.random.permutation(np.arange(n << 1))
	return p[:n], p[n:]

def Adapt(periodic: np.array, n: int) -> np.array:
	periodic -= np.min(periodic)
	periodic /= np.sum(periodic)
	num = np.zeros(n)
	for roll in np.random.choice(np.arange(n), n, p=periodic):
		num[roll] += 1
	return num.astype(int)

def Mutation(G: np.matrix, p: float) -> Tuple[np.matrix, int]:
	mask = np.random.uniform(size=g.shape) < p
	return g ^ mask, np.sum(np.sum(mask))

def Crossover(G: np.matrix, n: int, m_list: np.array, f_list: np.array):
	cros = np.random.randint(low=0, high=g.shape[1], size=n)
	g_cros = np.copy(g)
	for m, f, c in zip(m_list, f_list, cros):
		g_cros[[m, f], :c] = g_cros[[f, m], :c]
	return g_cros


if __name__ == "__main__":
	# mlist, flist = Parens(N)
	g_dec = np.matrix([[1.1, 2.31], [1.3, 2.7]])
	x_min = np.array([1, 2])
	nn = np.array([3, 4])
	dd = np.array([.1, .1])
	
	codbin = CodBinary(1.25, 1, 10, 0.1)
	print(f'codbin = CodBinary(1.25, 1, 10, 0.1):', codbin)
	print(f'CodDecimal(codbin, 1, 0.05):', CodDecimal(codbin, 1, 0.05))

	print(f'GenerationDec(3, 2, np.array([1, 1]), np.array([2, 2])): ', GenerationDec(3, 2, np.array([1, 1]), np.array([2, 2])) )
	nn, dd, NN = BinDecParam(3, 2, np.array([1, 1]), np.array([2, 2]), 0.01)
	print(f'BinDecParam nn: ', nn)
	print(f'BinDecParam dd: ', dd)
	print(f'BinDecParam NN: ', NN)

	periodic = np.array([1.1, 1.3, 1.7, 1.9])
	print("Adapt: ", Adapt(periodic, len(periodic)))

	print("Parens(10): ", Parens(10))
	
	# mutation 
	g = np.random.randint(low=0, high=2, size=(10, 20))
	g_mut, s_mut = Mutation(g, 1e-1)
	print(g_mut, s_mut, sep='\n')

	#crossover
	g = np.matrix([
		[1, 1, 1, 1, 1, 1], 
		[1, 1, 1, 1, 1, 1], 
		[0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0],
	])
	m_list, f_list = np.array([0, 1]), np.array([2, 3])
	print(Crossover(g, len(g)//2, m_list, f_list))
	

