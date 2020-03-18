#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.animation as animation


lambd: float = 220
c = 890
rho = 2700
alpha: float = lambd / (c * rho)
t_final: int = 10
gamma = 300
Rad: float = 0.01
T_env = 300
T0 = 0


class TimeRescaler:
    def __init__(self, a: float, r: float) -> None:
        self.a, self.r = a, r

    def t_to_t1(self, t: float) -> float:
        return self.a ** 2 * t / (self.r ** 2)

    def t1_to_t(self, t1: float) -> float:
        return self.r ** 2 * t1 / (self.a ** 2)


class TemperatureRescaler:
    def __init__(self, u_0: float, u_env: float) -> None:
        self.u_0, self.u_env = u_0, u_env

    def u_to_v(self, u: float) -> float:
        return (u - self.u_0) / (self.u_env - self.u_0)

    def v_to_u(self, v: float) -> float:
        return v * (self.u_env - self.u_0) + self.u_0


class RadiusRescaler:
    def __init__(self, r: float) -> None:
        self.r = r

    def x_to_x1(self, x: float) -> float:
        return x / self.r

    def x1_to_x(self, x1: float) -> float:
        return x1 * self.r


t_scaler = TimeRescaler(alpha, Rad)
u_scaler = TemperatureRescaler(u_0=T0, u_env=T_env)
x_scaler = RadiusRescaler(Rad)

N: int = 20
M: int = t_final * 2
h: float = Rad / N
tau: float = t_final / M
sigma = 0.5

beta2 = gamma / c / rho
mu2 = gamma * T_env/c/rho
q = gamma / c / rho

A_ = np.zeros((N+1, N+1))
b_ = np.zeros(N+1)

# t = t_scaler.t1_to_t(solver.t1)
# xs = np.array([x_scaler.x1_to_x(x1) for x1 in solver.x1s])
# us = np.array([u_scaler.v_to_u(v) for v in solver.vs])

def pi(i: int):
    return lambd/c/rho * (h * i - h/2)**2 

def tilde_x(i: int):
    if i == 0:
        return h**3 / (3*h)
    elif i == N:
        return (Rad**3 - (Rad-h)**3) / (3*h)
    return ((h*(i+1))**3 - (h*(i-1))**3) / (6*h)

def phii(i: int, y: np.array):
    if i == N+1:
        return (1-sigma)*tau/h*beta2*(h*N)**2*y[N]  -tau/h*mu2*(h*N)**2 -\
            1/2 * tilde_x(N) *y[N] + (1-sigma)*tau/2*tilde_x(N)*q*y[N]+\
            (1-sigma) *tau/h**2 * pi(N)*(y[N] - y[N-1])
    else:
        return -tilde_x(i-1)*y[i-1] - \
                tau*(1-sigma)/h**2*(pi(i) *(y[i] - y[i-1]) - pi(i-1)*(y[i-1] - y[i-2]))+\
                tau*(1-sigma) *tilde_x(i-1)*q*y[i-1]


def di(i: int):
    return sigma*tau/h**2 * pi(i-1)

def bi(i: int):
    return sigma*tau/h**2 * pi(i)

def ci(i: int):
    if i == N+1:
        return -sigma*tau/h*beta2*(h*N)**2 - 1/2*(h*N)**2 -\
            sigma*tau/2*tilde_x(N)*q - di(N+1)
    return -tilde_x(i-1) * (1 + tau*sigma*q) - (di(i) + bi(i))


print(f'alpha*tau/h^2 < 1/2: ({lambd/c/rho*tau/h**2}')


def count_one_layer(v: np.array):
    A_[0][0] = 1
    A_[0][1] = -1
    b_[0] = 0
    for i in range(1, N):
        b_[i] = phii(i+1, v)
        A_[i][i-1] = di(i+1)
        A_[i][i] = ci(i+1)
        A_[i][i+1] = bi(i+1)
    b_[N] = phii(N+1, v)
    A_[N][N-1] = di(N+1) 
    A_[N][N] = ci(N+1)
    return np.linalg.solve(A_, b_)

last_times = [M/4, M/3, M/2, M]
times_to_print = [0, 20, 50, M/2, M]

def count_temperature():
    v = np.ones(N+1)*T0
    for j in range(M):
        if j%100 == 0: 
            plt.plot(np.linspace(0, Rad, Rad/h+1), v)
        v = count_one_layer(v)
    print(f'y_0 = {v[0]}')
    print(f'y_N = {v[N]}')
    plt.plot(np.linspace(0, Rad, Rad/h+1), v)
    plt.xlabel('radius')
    plt.ylabel('temperature')
    plt.grid()
    plt.title(f'Temperature in {t_final} seconds')
    plt.show()
    return v

count_temperature()
