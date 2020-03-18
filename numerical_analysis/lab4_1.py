#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from typing import Callable
from trigonometry_functionality import LinearTrigonometricFunction, DifferentialOperator

a, b = 0, 2
m1, m2, m3, m4, m5 =  1, 1, 3, 3, 1
# m2 = 0
k1, k2, k3 = 1, 1, 2
p1, p2, p3 = 1, 1, 1
q1, q2, q3 = 1, 2, 2
alpha1, alpha2 = 1, 2
n = 5 # 5-7

def k(x: float) -> float:
    return k1 * np.power(x, k2) + k3

def p(x: float) -> float:
    return p1 * np.power(x, p2) + p3

def q(x: float) -> float:
    return q1 * np.power(x, q2) + q3

u_real = LinearTrigonometricFunction(m3, [[m1, m2]], [])
du_dx = DifferentialOperator(u_real, 1)
d2u_dx = DifferentialOperator(du_dx, 1)

print(f'u(x) = {u_real}')
print(f'u\'(x) = {DifferentialOperator(u_real, 1)}')
print(f'u\'\'(x) = {DifferentialOperator(u_real, 2)}')

mu1 = -k(a) * du_dx(a) + alpha1 * u_real(a)
mu2 = k(b) * du_dx(b) + alpha2 * u_real(b)

def f(x: float) -> float:
    #-(ku')'= - (k' * du + du*k) 
    return -(k1*k2*np.power(x, k2-1) * du_dx(x) + d2u_dx(x) * k(x)) + \
        p(x) * (du_dx(x)) + q(x) * u_real(x)

print(f'f(1) = {f(1)}')

def scalar_prod(f1: Callable[[float], float], f2: Callable[[float], float], lower: float, higher: float) -> float:
    return integrate.quad(lambda x: f1(x) * f2(x), lower, higher)[0]

def graph(x, f: Callable[[float], float], f_sol: Callable[[float], float], title: str):
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(x, f(x), 'k-', label='Real u(x)')
    ax.plot(x, f_sol(x), 'k-', label='u_n')
    plt.xlabel('x') 
    plt.ylabel('u')
    ax.legend(loc='upper left')
    plt.title(title)
    ax.grid()
    plt.show()


def phi(i: int, x: float):
    return (1-x) * x**i

def dphi(i: int, x: float):
    return - x**i + (1-x) * i * x**(i-1)

def d2phi(i: int, x: float):
    return -i*x**(i-1) - i* x**(i-1) + (1-x)*i* (i-1)*x**(i-2)

def operator_A(u, du, d2u, x):
    return -(k1*k2*np.power(x, k2-1) * du(x) + d2u(x) * k(x)) + \
        p(x) * (du(x)) + q(x) * u(x)


b_ = np.array([
    scalar_prod(f, lambda x: phi(i, x), a, b)
    for i in range(1,n+1)
])

A = np.array([
    [
        scalar_prod(
            lambda x: operator_A(phi, dphi, d2phi, x)
            lambda x: phi(j, x),
            a, b
        )
        for j in range(1, n+1)
    ]
    for i in range(1, n+1)
])

c = np.linalg.solve(A, b_)

print(f'Ax-b = {np.dot(A, c) - b_}')
print(f'c = {c}')

def u_n(x: float):
    return np.sum([c[i]*phi(i+1, x) for i in range(len(c))])

print(f'u(1) = {u_real(1)} | u_n(1)= {u_n(1)}, delta = {u_real(1)-u_n(1)}')
print(f'u(x) - u_n(0)={u_n(0)} = {u_real(0)-u_n(0)}')
print(f'u(x) - u_n(0.5)={u_n(0.5)} = {u_real(0.5)-u_n(0.5)}')


x = np.linspace(a, b, 100)
graph(x, u_real, u_real, 'Solutions')
