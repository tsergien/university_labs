# Genetic decode algoritm
import math
import numpy as np
import random

def generationDec(N, M):
    Xmin = []
    Xmax = []
    G = np.zeros( (N, M) )

    for i in range(N):
        for j in range(M-1):
            Xmin.append(j/M)
            Xmax.append(1/j + j/M) 
            G[i][j] = int(random.randint(Xmin[j], Xmax[j]))
    print(G)
    print("\033[1;33mXmin: \033[0;0m" + str(Xmin))
    print("\033[1;33mXmax: \033[0;0m" + str(Xmax))


def BinDecParam(Xmin, Xmax):
    pass

def CodBinary():
    pass

# Процедура выполняет кодирование любого действительного числа xdec из заданного диапазона [xmin..xmax] 
# c заданной точностью eps в последовательность из 0 и 1 фиксированной длины.
#  Процедура работает в паре с процедурой  CodDecimal, которая выполняет обратное 
# преобразование, вспомогательные параметры  вычисляются процедурой 
# xdec – десятичное число
# xmin, - минимальное значение кодируемого числа
# l – целое число, максимальное  количество двоичных разрядов для представления любого числа из заданного диапазона с заданной точностью.
# d –дискретность кодирования действительного числа xdec целым числом.
def CodDecimal(xdec, xmin, l, d):
    

if __name__ == "__main__":
    N = int(input("\033[1;33mPlease, enter N(rows):\033[0;0m "))
    M = int(input("\033[1;33mPlease, enter M(columns):\033[0;0m "))
    # N = 3
    # M = 5
    generationDec(N, M)