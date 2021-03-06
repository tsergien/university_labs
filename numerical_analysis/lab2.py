#!/usr/bin/python3

import numpy as np
from scipy import integrate
from typing import Callable

n = 3
m = 2
eps = 1e-5


def f(x: float) -> float:
    return np.power(x, n) / np.sqrt(1 - x**2)

# def g(x: float) -> float:
#     s2 = np.sqrt(2)
#     return (1-x)**(-1/2) / s2 * (1 - (4*n - 1)/4 * (1 - x))

def g(x: float) -> float:
    s2 = np.sqrt(2)
    return (1-x)**(-1/2) / s2 * (1 - (4*n - 1)/4 * (1 - x)) + \
    (16*n**2 - 24*n +3) / 32 / s2 * (x-1)**2

# def  psi(x: float) -> float:
#     s2 = np.sqrt(2)
#     return (np.power(x, n) / np.sqrt(1 + x) - 1 / s2) / np.sqrt(1-x) +\
#         (4*n - 1)/4/s2* np.power(1 - x, 1/2)


def  psi(x: float) -> float:
    return f(x) - g(x)

def integrate_rect(h: float, a: float, b: float, fun: Callable[[float], float]) -> float:
    x = np.arange(a, b, h)
    return np.sum(h* fun((x[1:] + x[:-1]) / 2))

def apriori_error(h: float, M_2: float, a:float, b: float) -> float:
    return M_2 * h * h * (b - a) / 24


if __name__ == "__main__":
    a = 0
    b = 1
    h = 0.2

    g_value = integrate.quad(g, a, b)[0]
    print("g(x) = ", g_value)

    I_h = integrate_rect(h, a, b, psi)
    I_h_half = integrate_rect(h / 2, a, b, psi)
    I_h_half = (2**m  *I_h_half - I_h) / (2**m - 1)
    R_h_half = (I_h_half - I_h) / (2**m - 1)

    while abs(R_h_half) >= eps/2:
        h = h / 2
        I_h = I_h_half
        I_h_half = integrate_rect(h / 2, a, b, psi)
        I_h_half = (2**m  * I_h_half - I_h) / (2**m - 1) 
        R_h_half = (I_h_half - I_h) / (2**m - 1)

    print(f' Integral value: {I_h}\n',
        f' I + g: {I_h + g_value}\n',
    f'Aposteriori error R(h): {eps / 2 + R_h_half}\n',
    f'h: {h}\n')


    M_2 = 36263903598
    h = np.sqrt(24* eps / M_2 / (b-a))
    print(f' Integral value psi: {integrate_rect(h, a, b, psi)}\n',
    f' Integral value: {g_value + integrate_rect(h, a, b, psi)}\n',
    f'Apriori error: {apriori_error(h, M_2, a, b)}\n',
    f'h: {h}\n')


