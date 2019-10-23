#!/usr/bin/env python3 

from sympy import *
import numpy as np
import matplotlib.pyplot as plt 
from typing import Callable
from scipy import integrate as scipy_int
import warnings
warnings.filterwarnings("ignore")

a, b = 0, 2
alpha1, alpha2 = 1, 2
n = 8 # 5-7
eps = 1e-10

x = Symbol('x')
k_expr = 1 * x**1 + 2
p_expr = 1 * x**1 + 1
q_expr = 1 * x**2 + 2
k = lambdify(x, k_expr, 'numpy')
p = lambdify(x, p_expr, 'numpy')
q = lambdify(x, q_expr, 'numpy')

u_expr = 3 * sin(5 * x) + 3
u_real = lambdify(x, u_expr, 'numpy') 
du = lambdify(x, u_expr.diff(x), 'numpy')


mu1 = -k(a) * du(a) + alpha1 * u_real(a)
mu2 = k(b) * du(b) + alpha2 * u_real(b)
print(f'mu_1 = {mu1}, mu_2 = {mu2}')



def operator_A(expr):
    return -(k_expr*expr.diff(x)).diff(x) + p_expr * expr.diff(x) + q_expr * expr


f_expr = operator_A(u_expr)
f = lambdify(x, f_expr, 'numpy')


print(f'Au = -(k(x)u(x)\')\' + p(x)u(x)\' + q(x)u(x)')
print(f'A = {operator_A(u_expr)}\n')
print(f'f = {f_expr}')



def graph(y, f_array, labels):
    ax = plt.subplot(111)
    colors = ['k-', 'b--', 'g--', 'r-', 'k.', 'b-', 'r.', 'g.']
    for i in range(len(f_array)):
        ax.plot(y, f_array[i](y), colors[i % 8], label=labels[i])
    plt.xlabel('x') 
    plt.ylabel('u')
    ax.legend(loc='upper left')
    plt.title('Solutions')
    ax.grid()
    plt.show()



def phi_i_expr(i: int):
    if i < 2:
        c, d = symbols('c d')
        c = b + (k(b) * (b-a))/(2*k(b) + alpha2 * (b-a))
        d = a - (k(a) * (b-a))/(2*k(a) + alpha1 * (b-a))
        if i == 0:
            return (x-a)**2 * (x-c)
        return (b-x)**2 * (x-d)
    l = Symbol('l')
    l = i
    return (x-a)**l * (b-x)**2


def phi_i(i: int, x: float):
    if i < 2:
        c = b + (k(b) * (b-a))/(2*k(b) + alpha2 * (b-a))
        d = a - (k(a) * (b-a))/(2*k(a) + alpha1 * (b-a))
        # print(f'c = {c}, d = {d}')
        if i == 0:
            return (x-a)**2 * (x-c)
        return (b-x)**2 * (x-d)
    return (x-a)**i * (b-x)**2


C, D  = symbols('C D')
C = (alpha2*mu1 - mu2*alpha1) / (alpha2*(alpha1*a-k(a)) - alpha1*(k(b) + alpha2*b))
D = (mu1 + k(a) * C) / alpha1 - C*a
phi0_expr = C * x + D
print(f'phi0 = {phi0_expr}')


def phi0(y: float):
    return C * y + D


def Galerkin():
    f_expr_v = f_expr - operator_A(phi0_expr)
    b_ = np.zeros((n, 1))
    A = np.zeros((n, n))
    for row in range(n):
        f_phi = lambdify(x, f_expr_v*phi_i_expr(row), 'numpy')
        b_[row] = scipy_int.quad(lambda y: f_phi(y), a, b, epsabs=eps, epsrel=eps, limit=100)[0]
        for col in range(n):
            temp_f = lambdify(x, operator_A(phi_i_expr(col)) * phi_i_expr(row), 'numpy')
            # graph(np.linspace(a, b, 50), [temp_f], [f'A(phi_{col} * phi_{row}'])
            A[row][col] = scipy_int.quad(lambda y: temp_f(y), a, b, epsabs=eps, epsrel=eps, limit=100)[0]
    coef = np.linalg.solve(A, b_)
    print(f'sum(Ax-b) = {sum(np.dot(A, coef) - b_)}')
    return coef


def least_squares():
    f_expr_v = f_expr - operator_A(phi0_expr)
    b_ = np.zeros((n, 1))
    A = np.zeros((n, n))
    for row in range(n):
        f_Aphi = lambdify(x, f_expr_v * operator_A(phi_i_expr(row)), 'numpy')
        b_[row] = scipy_int.quad(lambda y: f_Aphi(y), a, b, epsabs=eps, epsrel=eps, limit=100)[0]
        for col in range(n):
            temp_f = lambdify(x, operator_A(phi_i_expr(col))* operator_A(phi_i_expr(row)), 'numpy')
            A[row][col] = scipy_int.quad(lambda y: temp_f(y), a, b, epsabs=eps, epsrel=eps, limit=100)[0]
    coef = np.linalg.solve(A, b_)
    print(f'sum(Ax-b) = {sum(np.dot(A, coef) - b_)}')
    return coef


def count_stuff():
    coef = Galerkin()
    def u_n(y: float)->float:
        return sum([coef[i] * phi_i(i, y) for i in range(n)]) + phi0(y)

    coef_sq = least_squares()
    def u_n_squares(y: float)->float:
        return sum([coef_sq[i] * phi_i(i, y) for i in range(n)]) + phi0(y)

    graph(np.linspace(a, b, 100), [u_real, u_n, u_n_squares],
        ['u_real', 'Galerkin $u_{%i}$' % n, 'Least squares $u_{%i}$' % n])
    # graph(np.linspace(a, b, 50), [u_real, u_n], ['u_real', f'Galerkin u_{n}'])
    # graph(np.linspace(a, b, 50), [u_real, u_n_squares], ['u_real', f'Least squares u_{n}'])
    
    print(f'delta(Galerkin) = {scipy_int.quad(lambda y: abs(u_real(y) - u_n(y)), a, b, epsabs=eps, epsrel=eps, limit=100)}')
    print(f'delta(squares) = {scipy_int.quad(lambda y: abs(u_real(y) - u_n_squares(y)), a, b, epsabs=eps, epsrel=eps, limit=100)}')


count_stuff()

