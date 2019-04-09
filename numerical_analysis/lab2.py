#!/usr/bin/python3

import numpy as np

n = 2
a, b = 0, 1
m = 2
eps = 10**(-5)

def f(x: float) -> float:
    return np.power(x, n) / np.sqrt(1 - x**2)


def integrate_rect(h: float) -> float:
    x = np.arange(a, b, h)
    # print("-->: ", x)
    return np.sum(h* f((x[1:] + x[:-1]) / 2))

def apriori_error(h: float, M_2: float) -> float:
    return M_2 * h * h * (b - a) / 24

if __name__ == "__main__":
    h = 0.2
    I_h = integrate_rect(h)
    I_h_half = integrate_rect(h / 2)
    R_h_half = (I_h_half - I_h) / (2**m - 1)

    while abs(R_h_half) >= eps:
        h = h / 2
        I_h = integrate_rect(h)
        I_h_half = integrate_rect(h / 2)
        R_h_half = (I_h_half - I_h) / (2**m - 1)
        print(f' Integral value: ', I_h,'\n',
        f'Error: ', R_h_half,'\n',
        f'h: ', h, '\n')

    # M_2 = 100
    # h = 0.4
    # while apriori_error(h, M_2) >= eps:
    #     h = h / 2
    #     print(f' Integral value: ', I_h,'\n',
    #         f'Apriori error: ', R_h_half,'\n',
    #         f'h: ', h, '\n')
        



