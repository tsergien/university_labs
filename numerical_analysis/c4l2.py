#!/usr/bin/env python3

from sympy import Symbol, diff, lambdify, sin
import numpy as np
import matplotlib.pyplot as plt 
from typing import Callable
from scipy import integrate as scipy_int

import warnings
warnings.filterwarnings("ignore")

a, b = 0, 2
alpha1, alpha2 = 1, 2

x = Symbol('x')
u_expr = 1 * sin(7 * x) + 3
u_exact = lambdify(x, u_expr, 'numpy') 
du = lambdify(x, u_expr.diff(x), 'numpy')


k_expr = 1 * x**1 + 2
p_expr = 1 * x**1 + 1
q_expr = 1 * x**2 + 2
k = lambdify(x, k_expr, 'numpy')
p = lambdify(x, p_expr, 'numpy')
q = lambdify(x, q_expr, 'numpy')
def operator_A(expr):
    return -(k_expr*expr.diff(x)).diff(x) + p_expr * expr.diff(x) + q_expr * expr
f_expr = operator_A(u_expr)
f = lambdify(x, f_expr, 'numpy')

mu1 = -k(a) * du(a) + alpha1 * u_exact(a)
mu2 = k(b) * du(b) + alpha2 * u_exact(b)

N = 100
h = (b-a)/N
print(f'h = {h}')
A_ = np.zeros((N+1, N+1))
b_ = np.zeros(N+1)


def ai(i: int):
    return k(a + h * i - h/2)

def bi(i: int):
    return p(a + h * i - h/2) / 2

def di(i: int):
    return q(a + h * i)

def psii(i: int):
    return f(a + h * i)



A_[0][0] = ai(1)/h - bi(1) + (h/2)* di(0) + alpha1
A_[0][1] = -ai(1)/h + bi(1)
b_[0] = (h/2) * psii(0) + mu1

for j in range(1, N):
    xj = a + j * h
    A_[j][j-1] = -ai(j) / (h**2) - bi(j) / h
    A_[j][j] = (ai(j)+ai(j+1)) / (h**2) + (bi(j) - bi(j+1)) / h  + di(j)
    A_[j][j+1] = -ai(j+1) / (h**2) + bi(j+1) / h
    b_[j] = psii(j)

A_[N][N-1] = -ai(N) /h - bi(N)
A_[N][N] = ai(N)/h +bi(N) + h/2*di(N) + alpha2
b_[N] = h/2*psii(N) + mu2

y = np.linalg.solve(A_, b_)
print(f'Ay -b : {sum((np.dot(A_, y) - b_)**2)}')

dec = 5
print(' i  \t\t\t\t  u  \t\t\t\t  y  \t\t\t\t\t  delta ')
for j in range(N+1):
    xj = a + h*j
    if j % (N/10) == 0:
        print(f'{round(xj, dec)} \t\t\t\t {round(u_exact(xj), dec)} \t\t\t\t {round(y[j], dec)} \
        \t\t\t\t {abs(round(u_exact(xj) - y[j], 7))}')
    

def graph(xi, f, y_values, labels):
    ax = plt.subplot(111)
    ax.plot(xi, f(xi), 'r', label=labels[0])
    ax.scatter(xi, y_values, c='k', label=labels[1])

    plt.xlabel('x') 
    plt.ylabel('u')
    ax.legend(loc='upper left')
    plt.title(f'Solutions (N= {N})')
    ax.grid()
    plt.show()


graph(np.linspace(a, b, N+1), u_exact, y,
        ['u_real', 'y_values'])
