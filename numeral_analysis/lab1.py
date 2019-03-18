#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from math import pi
from typing import Callable, List

a, b = 0, 5
A, B, w = 1, 1, 2

def f(x: float) -> float:
    return A * np.sin(w * x) + B * x

def scalar_prod(f1: Callable[[float], float], f2: Callable[[float], float], lower: float, higher: float) -> float:
    return integrate.quad(lambda x: f1(x) * f2(x), lower, higher)[0]

def rescale_function(old_a: float, old_b: float, f: Callable[[float], float], 
    new_a: float, new_b: float) -> Callable[[float], float]:
    return lambda x: f((old_b - old_a) / (new_b - new_a) * (x - new_a) + old_a)

def graph(x, f: Callable[[float], float], f_sol: Callable[[float], float], name: str):
    plt.plot(x, f_sol(x), 'k-', label='Approximation function')
    plt.plot(x, f(x), 'b-', label='True function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(name)
    plt.ylim((-0.5, 5.5))
    plt.legend()
    plt.grid(True)
    plt.show()

def root_mean_square_approximation(a0: float, b0: float, 
    phi: Callable[[int, float], float],
    f: Callable[[float], float]) -> Callable[[float], float]:

    b = np.array([
        scalar_prod(f, lambda x: phi(i, x), a0, b0)
        for i in range(n)
    ])

    a = np.array([
        [
            scalar_prod(
                lambda x: phi(i, x),
                lambda x: phi(j, x),
                a0, b0
            )
            for j in range(n)
        ]
        for i in range(n)
    ])

    c = np.linalg.solve(a, b)

    def f_sol(x):
        return np.dot(c, np.array([phi(k, x) for k in range(n)]))
    return f_sol


def polinomial():
    def phi(i: int, x: float) -> float:
        return x**i
    f_sol = root_mean_square_approximation(a, b, phi, f)
    print(f'Polynomial approximation error = '
        f'{integrate.quad(lambda x: (f_sol(x) - f(x))**2, a, b)[0]}')
    x = np.linspace(a, b, 100)
    graph(x, f, f_sol, "Polinomial approximation")


def trigonometric():
    a0, b0, f_resc = -pi, pi, rescale_function(a, b, f, -pi, pi)
    def phi(i: int, x: float) -> float:
        return (np.sin if (i & 1) else np.cos)(((i + 1) >> 1) * x)
    f_sol = root_mean_square_approximation(a0, b0, phi, f_resc)
    print(f'Trigonometric approximation error = '
        f'{integrate.quad(lambda x: (f_sol(x) - f_resc(x))**2, a0, b0)[0]}')
    x = np.linspace(a, b, 100)
    f_sol = rescale_function(-pi, pi, f_sol, a, b)
    graph(x, f, f_sol, "Trigonometric approximation")


####################################################################
########################## PART 2 ##################################
def scalar_product_discrete(f1: Callable[[float], float], f2: Callable[[float], float], 
    x: List[float]) -> float:
    return np.dot(list(map(f1, x)), list(map(f2, x))) / len(x)

def root_mean_square_approximation_polinomial_discrete(n_dots: int, m: int, a0: float, 
    b0: float) -> None:
    x = np.linspace(a0, b0, n_dots + 1)
    
    # cost = [np.inf for _ in range(10)]
    cost = np.inf
    cost_prev = np.unf
    for n in range(1, 10):
    while cost
        b = np.array([
            scalar_product_discrete(f, lambda x: x**i, x)
        for i in range(n + 1)])

        a = np.array([[
            scalar_product_discrete( 
                lambda x: x**j, 
                lambda x: x**i,
                x) for j in range(n + 1)
        ] for i in range(n + 1)])

        c = np.linalg.solve(a, b)

        def f_sol(x):
            s = 0
            x_pow = 1
            for k in range(n + 1):
                s += c[k] * x_pow
                x_pow *= x
            return s

        def diff(x): 
            return f(x) - f_sol(x)

        cost[n] = scalar_product_discrete(diff, diff, x) / (n_dots - m)

        print(f'n = {n}, cost = {cost[n]}')

    # true value of n
    n = 2  # cost.index(min(cost))

    b = np.array([
        scalar_product_discrete(f, lambda x: x**i, x)
    for i in range(n + 1)])

    a = np.array([[
        scalar_product_discrete(
            lambda x: x**j, 
            lambda x: x**i, 
            x) for j in range(n + 1)
    ] for i in range(n + 1)])

    c = np.linalg.solve(a, b)

    def f_sol(x):
        s = 0
        x_pow = 1
        for k in range(n + 1):
            s += c[k] * x_pow
            x_pow *= x
        return s

    def diff(x):
        return f(x) - f_sol(x)

    x = np.linspace(a0, b0, 100)
    graph(x, f, f_sol, "Discrete approximation")


########################################################################
############################### PART 3 #################################
def spline_interpolation(n: int, a0: float, b0: float, 
    f: Callable[[float], float]) -> None:
    x = np.linspace(a0, b0, n + 1)
    h = x[1:] - x[:-1]

    R = np.eye(n + 1)

    H = np.zeros((n + 1, n + 1))

    for i in range(1, n):
        H[i][i - 1] = 1 / h[i - 1]
        H[i][i] = - (1 / h[i - 1] + 1 / h[i])
        H[i][i + 1] = 1 / h[i]

    a = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)    

    for i in range(n + 1):
        if i == 0 or i == n:
            a[i, i] = 1
        else:
            a[i, i - 1] = h[i - 1] / 6
            a[i, i] = (h[i - 1] + h[i]) / 3
            a[i, i + 1] = h[i] / 6
            b[i] = (f(x[i + 1]) - f(x[i])) / h[i] - (f(x[i]) - f(x[i - 1])) / h[i - 1]

    m = np.linalg.solve(a + np.dot(H, H.T), b)

    f_u = f(x) - np.dot(H.T, m).T

    def f_sol(x0: float) -> float:
        for i in range(n):
            if x[i + 1] >= x0 >= x[i]:
                return m[i] * ((x[i + 1] - x0)**3) / (6 * h[i]) + \
                    m[i + 1] * ((x0 - x[i])**3) / (6 * h[i]) + \
                    (f_u[i] - m[i] * h[i]**2 / 6) * (x[i + 1] - x0) / h[i] + \
                    (f_u[i + 1] - m[i + 1] * h[i]**2 / 6) * (x0 - x[i]) / h[i]

    x1 = np.linspace(a0, b0, 100 + 1)
    y = [f_sol(xi) for xi in x1]

    plt.plot(x1, y, 'k-', label='Approximation function')
    plt.plot(x1, f(x1), 'b-', label='True function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Spline interpolation")
    plt.ylim((-0.5,5.5))
    plt.legend()
    plt.grid(True)
    plt.show()


n = 5
polinomial()
trigonometric()
n_disc, m = 12, 5
root_mean_square_approximation_polinomial_discrete(n_disc, m, a, b)
n_spl = 10
# spline_interpolation(n_spl, a, b, f)
