#!/usr/bin/python3

import math
import numpy as np
import random
from functools import reduce

dd = []
nn = []
NN = []

def CodBinary(xdec: float, xmin: float, l: int, d: float) -> np.array:
    """
    :param x_dec: dec num to encode
    :param x_min: min num possible to encode
    :param l: num of bin digits to return
    :param d: discretionary of encoding to return
    :return: encoded num as np.array of digits
    """
    xx = int(np.floor((xdec - xmin) / d))
    digits = list(map(int, bin(xx)[:1:-1]))
    return np.array(digits + [0 for _ in range(l - len(digits))])



def CodDecimal(xbin: np.array, xmin: float, d: float):
    """
    :param x_bin: bin num to decode as np.array of digits
    :param x_min: min num possible to encode
    :param d: discretionary of encoded number
    :return: decoded num as float
    """
    xdec1 = reduce(lambda _1, _2: _1 * 2 + _2, map(int, xbin[::-1]))
    return xmin + d * xdec1
    
def a_cod_binary(g_dec: np.matrix, x_min: np.array, nn: np.array, 
                 dd: np.array) -> np.matrix:
    """
    :param g_dec: dec nums matrix to encode
    :param x_min: min nums possible to encode
    :param nn: num bin digits to encode nums
    :param dd: discretionaries of encodings
    :return: encoded nums as np.matrix of np.arrays of digits
    """
    assert g_dec.ndim == 2, f"g_dec should be a matrix (have dimension 2). " + \
                            f"got g_dec.ndim = {g_dec.ndim}, g_dec = {g_dec}"
    assert x_min.ndim == 1, "x_min should be an array (have dimension 1)"
    assert nn.ndim == 1, "nn should be an array (have dimension 1)"
    assert dd.ndim == 1, "dd should be an array (have dimension 1)"
    assert g_dec.shape[1] == x_min.shape[0], "g_dec and x_min shapes mismatch"
    assert g_dec.shape[1] == nn.shape[0], "g_dec and nn shapes mismatch"
    assert g_dec.shape[1] == dd.shape[0], "g_dec and dd shapes mismatch"
    n, m = g_dec.shape

    return __a_cod_binary(n, m, g_dec, x_min, nn, dd)



def __a_cod_binary(n: int, m: int, g_dec: np.matrix, x_min: np.array,
                   nn: np.array, dd: np.array) -> np.matrix:
    """
    :param n: num rows in g_dec
    :param m: num cols in g_dec
    :param g_dec: dec nums matrix to encode
    :param x_min: min nums possible to encode
    :param nn: num bin digits to encode nums
    :param dd: discretionaries of encodings
    :return: encoded nums as np.matrix of np.arrays of digits
    """
    assert x_min.shape == (m, ), "x_min should be of shape (m, )"
    assert nn.shape == (m, ), "nn should be of shape (m, )"
    assert dd.shape == (m, ), "dd should be of shape (m, )"
    assert g_dec.shape == (n, m), "g_dec should be of shape (n, m)"

    return np.matrix([
        np.hstack([
            CodBinary(g_dec[i, j], x_min[j], nn[j], dd[j]) for j in range(m)
        ]) for i in range(n)
    ])




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
    N = int(input("\033[1;33mPlease, enter N(rows):\033[0;0m "))
    M = int(input("\033[1;33mPlease, enter M(columns):\033[0;0m "))

    mlist, flist = Parens(N)
    g_dec = np.matrix([[1.1, 2.31], [1.3, 2.7]])
    x_min = np.array([1, 2])
    nn = np.array([3, 4])
    dd = np.array([.1, .1])
    print( a_cod_binary(g_dec, x_min, nn, dd))


