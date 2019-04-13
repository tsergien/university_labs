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

def Parens(N: int):
    random.seed(1234)
    mlist = [random.randint(1, 2* N) for _ in range(N)]
    flist = [random.randint(1, 2 * N) for _ in range(N)]
    for i in range(N):
        if mlist[i] == flist[i]:
            mlist[i] = (mlist[i] + random.randint(1, 2*N)) % (N + 1)
    return (mlist, flist)


def Adapt(periodic: list, N: int):
    periodic_min = min(periodic)
    periodic = [periodic[i] - periodic_min for i in range(len(periodic))]


if __name__ == "__main__":
    # mlist, flist = Parens(N)
    g_dec = np.matrix([[1.1, 2.31], [1.3, 2.7]])
    x_min = np.array([1, 2])
    nn = np.array([3, 4])
    dd = np.array([.1, .1])
    
    codbin = CodBinary(1.25, 1, 10, 0.1)
    print(f'CodBinary:', codbin)
    print(f'CodDecimal:', CodDecimal(codbin, 1, 0.05))

    print(f'GenerationDec: ', GenerationDec(3, 2, np.array([1, 1]), np.array([2, 2])) )
    nn, dd, NN = BinDecParam(3, 2, np.array([1, 1]), np.array([2, 2]), 0.01)
    print(f'BinDecParam nn: ', nn)
    print(f'BinDecParam dd: ', dd)
    print(f'BinDecParam NN: ', NN)

