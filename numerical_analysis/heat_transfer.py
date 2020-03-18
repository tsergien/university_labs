#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.animation as animation


Rad: float = 0.5
n: int = 20 # nodes for radius
T_env = -20
T0 = 20
dx: float = Rad / n
lambd: float = 0.77
alpha: float = lambd / (0.83 * 1600)
t_final = 3600
dt = 0.01
gamma = 7

dudt = np.empty(n)


def solve_task():
    T = np.ones(n) * T0
    for j in range(int(t_final/dt)):
        if  j % 6000 == 0:
            plt.plot(np.linspace(dx/2, Rad-dx/2, n), T)
            # plt.legend(f'{j*dt}')
        for i in range(1, n-1):
            dudt[i] = alpha/dx**2 * (T[i-1] - 2*T[i] + T[i+1]) * dt
        dudt[0] = alpha/dx**2 * (2*T[1] - 2*T[0] )* dt
        dudt[n-1] = 0
        T += dudt
        T[n-1] = (T[n-2]+ gamma*dx/lambd*T_env) / (1 + gamma*dx/lambd)
    plt.plot(np.linspace(dx/2, Rad-dx/2, n), T)
    plt.xlabel('radius')
    plt.ylabel('temperature')
    plt.title('Temperature')
    plt.show()


def get_layer():
    for i in range(1, n-1):
        dudt[i] = alpha * ( (get_layer.T[i-1] - 2*get_layer.T[i] + get_layer.T[i+1])/dx**2)
    dudt[0] = alpha * (2*get_layer.T[1] - 2*get_layer.T[0] )/dx**2
    dudt[n-1] = alpha * (gamma*(get_layer.T[n-2] - 2*get_layer.T[n-1]+ T_env)/dx**2)
    get_layer.T += dudt * dt
    # print(f'{get_layer.T}')
    return get_layer.T

get_layer.T = np.ones(n) * T0


def build_animation():
    fig = plt.figure(figsize=(16, 9), dpi=70)
    ax = fig.add_subplot(111, projection='3d')
    theta = np.linspace(0, 2*np.pi, n)
    r = np.linspace(dx/2, Rad - dx/2, n)
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

        layer = get_layer()[:n]
        # layer = np.flip(layer, 0)
        Z = np.array([layer for k in range(n)])
        icecream = ax.plot_surface(X, Y, Z, cmap=cm.plasma, alpha=0.7, linewidth=0, antialiased=False)
        return icecream


    pause = True
    def onClick(event):
        global pause
        if pause:
            ani.event_source.stop()
        else:
            ani.event_source.start()
        pause ^= True

    fig.canvas.mpl_connect('button_press_event', onClick)
    ani = animation.FuncAnimation(fig, animate, frames=t_final, interval=10, blit=False)
    plt.show()

# solve_task()
build_animation()