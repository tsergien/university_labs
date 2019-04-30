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
u1_0 = 1+d
u2_0 = a+c
u3_0 = a*a + 2*b

def accurate_solution(x: float):
    return np.exp(a*x) + b * np.power(x, 2) + c*x + d

def f(x: float):
    eax = np.exp(a*x)
    return a**3 * eax + k * x * a * a * eax +\
        2 * k * b * x + np.power(a* eax + 2*b*x + c, 2) +\
        n * eax  + n* b * np.power(x, 2) + n*c*x + n*d

def y_n(y_n: float):
    
    return y_n + h * ()


x = np.linspace(0, 1, 100)
plt.plot(x, accurate_solution(x), 'k-', label='True function')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Accurate solution")
plt.legend()
plt.grid(True)
plt.show()


