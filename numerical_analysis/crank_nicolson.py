#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.animation as animation


lambd: float = 0.77
c = 830
rho = 1600
alpha: float = lambd / (c * rho)
t_final: int = 3600
gamma = 7
Rad: float = 0.5
T_env = -20
T0 = 20


N: int = 50
M: int = t_final * 4
h: float = Rad / N
tau: float = t_final / M
sigma = 0.5 - h**2/12/tau
print(f'h = {h} (^4 = {h**4}), tau = {tau} (^2 = {tau**2})')
print(f'sigma {sigma}')

beta2 = gamma/c/rho
mu2 = gamma * T_env/c/rho
q = gamma / c / rho

A_ = np.zeros((N+1, N+1))
b_ = np.zeros(N+1)


def pi(i: int):
    return lambd/c/rho * (h * i - h/2)**2 

def tilde_x(i: int):
    if i == 0:
        return h**2 / (2*h)
    elif i == N:
        return (Rad**2 - (Rad-h)**2) / (2*h)
    return ((h*(i+1))**2 - (h*(i-1))**2) / (4*h)

def phii(i: int, y: np.array):
    if i == N+1:
        return (1-sigma)*tau/h*beta2*h*N*y[N]  -tau/h*mu2*h*N -\
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
        return -sigma*tau/h*beta2*h*N - 1/2*h*N -\
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



def get_layer(i: int):
    if i == 0:
        return np.ones(N+1)*T0
    get_layer.T = count_one_layer(get_layer.T)
    return get_layer.T

get_layer.T = np.ones(N+1) * T0



def build_animation():
    fig = plt.figure(figsize=(16, 9), dpi=70)
    ax = fig.add_subplot(111, projection='3d')
    theta = np.linspace(0, 2*np.pi, N+1)
    r = np.linspace(0, Rad, N+1)
    R, P = np.meshgrid(r, theta)
    X, Y = R*np.cos(P), R*np.sin(P)

    def animate(i: int):
        ax.clear()
        plt.title("t = {0}".format(i))
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('temperature')
        ax.set_xlim(-.5, .5)
        ax.set_ylim(-.5, .5)
        ax.set_zlim(-20, 20)

        layer = get_layer(i)
        Z = np.array([layer for k in range(N+1)])
        icecream = ax.plot_surface(X, Y, Z, cmap=cm.plasma, alpha=0.5, linewidth=0, antialiased=False)
        return icecream


    ani = animation.FuncAnimation(fig, animate, frames=M, interval=10, blit=False)
    # Writer = animation.writers['ffmpeg']
    # writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    # ani.save('ice_cream.mp4', writer=writer)
    plt.show()


count_temperature()
build_animation()

