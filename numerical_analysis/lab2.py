#!/usr/bin/python3

import numpy as np

n = 2
m = 2
eps = 10**(-5)

def f(x: float) -> float:
    return np.power(x, n) / np.sqrt(1 - x**2)

def integrate_rect(h: float, a: float, b: float) -> float:
    x = np.arange(a, b, h)
    return np.sum(h* f((x[1:] + x[:-1]) / 2))

def apriori_error(h: float, M_2: float) -> float:
    return M_2 * h * h * (b - a) / 24

def second_derivative(x: float):
    return (n-1) * n * x**(n-2) / (1-x**2)**(0.5) + \
            x**n * (3 * x**2 / (1-x**2)**2.5 + 1 / (1-x**2)**1.5 ) + \
            2 * n * x**n / (1 - x**2)**1.5

if __name__ == "__main__":
    delta = eps/500
    a = 0
    b = 1 - delta
    h = 0.2
    I_h = integrate_rect(h, a, b)
    I_h_half = integrate_rect(h / 2, a, b)
    R_h_half = (I_h_half - I_h) / (2**m - 1)


    while abs(R_h_half) >= eps/2:
        h = h / 2
        I_h = I_h_half
        I_h_half = integrate_rect(h / 2, a, b)
        R_h_half = (I_h_half - I_h) / (2**m - 1)

    analytic_value = np.arcsin(1) - np.arcsin(1-delta)
    print("delta: ", delta)
    print("Analytic: ", analytic_value)
    print("I_h: ", I_h)
    I_h += analytic_value
    print(f' Integral value: ', I_h,'\n',
    f'Aposteriori error R(h): ', eps / 2 + R_h_half,'\n',
    f'h: ', h, '\n')

    M_2 = second_derivative(1 - delta)
    h = 0.4
    while apriori_error(h, M_2) >= eps:
        h = h / 2
    print(f' Integral value: ', integrate_rect(h, a, b),'\n',
    f'Apriori error: ', R_h_half,'\n',
    f'h: ', h, '\n')
        



