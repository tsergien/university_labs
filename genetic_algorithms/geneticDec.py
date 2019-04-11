#!/usr/bin/python3

import math
import numpy as np
import random

dd = []
nn = []
NN = []

def generationDec(N, M):
    Xmin = []
    Xmax = []
    G = np.zeros( (N, M+1) )

    for i in range(N):
        for j in range(M):
            Xmin.append(-5)
            Xmax.append(5) 
            G[i][j] = random.uniform(Xmin[j], Xmax[j])
    print("\033[1;33m Matrix G: \033[0;0m")
    print(G)
    print("\033[1;33mXmin: \033[0;0m" + str(Xmin))
    print("\033[1;33mXmax: \033[0;0m" + str(Xmax))
    BinDecParam(Xmin, Xmax, 0.001)
    return G

def CodBinary(xdec, xmin, l, d):
    print("initial xdec: ", xdec)
    Xbin = [] ############ fill later
    xx = (xdec - xmin) // d
    xx = bin(xx)
    if len(xx) < l:
        xx += "0" * (l - len(xx))
    print("xx: " , xx[2:])
    return xx[2:]

def CodDecimal(xbin, xmin, d):
    xdec1 = int(xbin, 2)
    xdec = xmin + d * xdec1
    print("xdec1: ", xdec1)
    print("xdec: ", xdec)
    return xdec
    
def BinDecParam(Xmin, Xmax, eps):
    dim = len(Xmin)
    NN.append(0)
    for i in range(dim):
        nn.append( int(math.log2((Xmax[i] - Xmin[i]) / eps) ) + 1 )
        dd.append( (Xmax[i] - Xmin[i]) / 2**nn[i] )
        NN.append( sum(nn) ) # NN[i] is l for CodBinary
    print("nn-------------->: ", nn)
    print("dd-------------->: ", dd)
    print("NN-------------->: ", NN)
    b = CodBinary(1.5, 0, 1, 3)
    CodDecimal(b, 0, 3)

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
    # N = int(input("\033[1;33mPlease, enter N(rows):\033[0;0m "))
    # M = int(input("\033[1;33mPlease, enter M(columns):\033[0;0m "))
    # G = generationDec(N, M)
    N = 10
    mlist, flist = Parens(N)
    

