#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

l = 1
a = 2
b = -2
c = 3
d = 1
k = 3
n = 1.5
u_0 = 1+d
u1_0 = a+c
u2_0 = a*a + 2*b

def accurate_solution(x: float):
    return np.exp(a*x) + b * np.power(x, 2) + c*x + d

def f(x: float):
    eax = np.exp(a*x)
    return a**3 * eax + k * x * a * a * eax +\
        2 * k * b * x + np.power(a* eax + 2*b*x + c, 2) +\
        n * eax  + n* b * np.power(x, 2) + n*c*x + n*d

def F(x :float, u :float, u1: float, u2: float):
    return f(x) - k*x*u2 - u1*u1 - n*u

x = np.linspace(0, l, 100)
plt.plot(x, accurate_solution(x), 'k-', label='True function')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Accurate solution")
plt.legend()
plt.grid(True)
plt.show()


h = 0.1
x = np.linspace(0, l,  step=h)
u = np.array()
u.append(u2_0)
for _ in range(l/h):
    y_i.append()
