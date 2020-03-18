#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

l: float = 2
a = 2
b = -2
c = 3
d = 1
k = 3
n = 1.5

def accurate_solution(x: float):
    return np.exp(a*x) + b * np.power(x, 2) + c*x + d

def f0(x: float):
    eax = np.exp(a*x)
    return a**3 * eax + k * x * a * a * eax +\
        2 * k * b * x + np.power(a* eax + 2*b*x + c, 2) +\
        n * eax  + n* b * np.power(x, 2) + n*c*x + n*d

def f(x: float, u: float, y: float, z: float):
    return f0(x) - k*x*z - y*y - n*u

def g(x: float, u: float, y: float, z: float):
        return z

def p(x: float, u: float, y: float, z: float):
        return y 

def r(value: float):
        return "{0:.2f}".format(value)

h = 0.01
x0 = 0
u_0 = 1 + d
y_0 = a+c # y = u' = f
z_0 = a*a + 2*b # z = u'' = g

values = []
print(f'l/h = {l/h}')
x_m = np.linspace(0, l+h, l/h)

print("\tx_i\t\tu(x_i)\t\tdelta(u)")
while x0 < l:
        k1 = h * f(x0, u_0, y_0, z_0) # z
        q1 = h * g(x0, u_0, y_0, z_0) # y
        s1 = h * p(x0, u_0, y_0, z_0) # u

        k2 = h * f(x0 + h/2.0, u_0 + s1/2.0, y_0 + q1/2.0, z_0 + k1/2.0)
        q2 = h * g(x0 + h/2.0, u_0 + s1/2.0, y_0 + q1/2.0, z_0 + k1/2.0)
        s2 = h * p(x0 + h/2.0, u_0 + s1/2.0, y_0 + q1/2.0, z_0 + k1/2.0)

        q3 = h * g(x0 + h/2.0, u_0 + s2/2.0, y_0 + q2/2.0, z_0 + k2/2.0)
        k3 = h * f(x0 + h/2.0, u_0 + s2/2.0, y_0 + q2/2.0, z_0 + k2/2.0)
        s3 = h * p(x0 + h/2.0, u_0 + s2/2.0, y_0 + q2/2.0, z_0 + k2/2.0)

        k4 = h * f(x0 + h, u_0 + s3, y_0 + q3, z_0 + k3)
        q4 = h * g(x0 + h, u_0 + s3, y_0 + q3, z_0 + k3)
        s4 = h * p(x0 + h, u_0 + s3, y_0 + q3, z_0 + k3)

        z_1 = z_0 + (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
        y_1 = y_0 + (q1 + 2.0*q2 + 2.0*q3 + q4)/6.0
        u_1 = u_0 + (s1 + 2.0*s2 + 2.0*s3 + s4)/6.0
        print(f'\t {r(x0)}\t\t{r(u_0)}\t\t{accurate_solution(x0) - u_0}')
        values.append(u_0)
        u_0 = u_1
        y_0 = y_1
        z_0 = z_1
        x0 += h

x = np.linspace(0, l, 100)
plt.plot(x, accurate_solution(x), 'k-', label='True function')
plt.plot(x_m, values, 'b-', label='Runge-Kutta')
plt.plot(x_m, values - accurate_solution(x_m), 'r.', label='Error')
plt.xlabel('x')
plt.ylabel('u')
plt.title(f'Solutions (h = {h})')
plt.legend()
plt.grid(True)
plt.show()
        

