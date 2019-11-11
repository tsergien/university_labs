#!/usr/bin/env python3

# was created by Ihor Onyshchenko. 2018.

import numpy as np
import random as rd
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.animation as animation


class Model:
    def __init__(self, dim, LG_index, y_index, time, x_min, x_max, y_min=0, y_max=0):
        self.dim = dim
        self.time = int(time)
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.c = 1  # for G
        self.LG_index = LG_index
        self.y_index = y_index

        if self.y_index == 0:
            self.y = lambda s: np.cos(s[0]) + np.sin(2*s[1])  # true solution
        elif self.y_index == 1:
            self.y = lambda s: 3*np.cos(2*s[0])*np.sin(s[1])*np.cos(s[-1]/2)
        else:
            self.y = lambda s: 0
            
        self.L0 = 0
        self.X_L0 = []
        self.Y_L0 = []

        self.LG = 0
        self.X_LG = []
        self.Y_LG = []

        self.Y = []

        self.M0 = 0
        self.S_m0 = []

        self.MG = 0
        self.S_mG = []

        self.u0 = []
        self.uG = []

        self.calculated = False
        self.precision = 10e-3

    def my_abs(self, s):
        return sum([e * e for e in s[:-1]]) ** 0.5

    def __G_3d(self, s):
        param = self.c * s[-1] - self.my_abs(s)
        if param > 0:
            return 1 / (2 * math.pi * self.c) / (self.c ** 2 * s[-1] ** 2 - self.my_abs(s) ** 2)
        return 0

    def __G_2d(self, s):
        param = self.c * s[-1] - self.my_abs(s)
        if param > 0:
            return 0.5 / self.c
        return 0

    def G(self, s):
        if self.dim == 2:
            return self.__G_2d(s)
        elif self.dim == 3:
            return self.__G_3d(s)
        return 0

    def set_func(self, f):
        self.y = f

    def __check_for_ndarr(self, arr):
        return type(arr) == np.ndarray

    def set_start_conditions(self, arrX):
        self.X_L0 = np.array(arrX)

        self.L0 = len(arrX)
        # self.Y_L0 = np.array(list(map(self.y, self.X_L0))) + self.precision
        self.Y_L0 = np.array([self.y(self.X_L0[i]) + self.precision for i in range(self.L0)])

    def set_border_conditions(self, arrX):
        self.X_LG = np.array(arrX)

        self.LG = len(arrX)

        self.Y_LG = np.array([self.y(self.X_LG[i]) + self.precision for i in range(self.LG)])

    def set_points_sm0(self, arr):
        self.S_m0 = np.array(arr)

        self.M0 = len(arr)

    def set_points_smG(self, arr):
        if self.__check_for_ndarr(arr):
            self.S_mG = arr
        else:
            self.S_mG = np.array(arr)

        self.MG = len(arr)

    def __calculate(self):
        Y0 = np.array([self.Y_L0[i] - self.y(self.X_L0[i]) for i in range(self.L0)])
        YG = np.array([self.Y_LG[i] - self.y(self.X_LG[i]) for i in range(self.LG)])
        self.Y = np.concatenate((Y0, YG))

        A11 = np.array([[self.G(self.X_L0[j] - self.S_m0[i]) for i in range(self.M0)] for j in range(self.L0)])
        A12 = np.array([[self.G(self.X_L0[j] - self.S_mG[i]) for i in range(self.MG)] for j in range(self.L0)])
        A21 = np.array([[self.G(self.X_LG[j] - self.S_m0[i]) for i in range(self.M0)] for j in range(self.LG)])
        A22 = np.array([[self.G(self.X_LG[j] - self.S_mG[i]) for i in range(self.MG)] for j in range(self.LG)])

        A = np.hstack((np.vstack((A11, A21)), np.vstack((A12, A22))))

        P1 = np.dot(A, np.transpose(A))
        invP1 = np.linalg.pinv(P1)

        v = np.array([0 for i in range(self.M0 + self.MG)])
        self.u0 = np.dot(np.dot(np.hstack((np.transpose(A11), np.transpose(A21))), invP1), (self.Y - np.dot(A, v)))
        self.uG = np.dot(np.dot(np.hstack((np.transpose(A12), np.transpose(A22))), invP1), (self.Y - np.dot(A, v)))

        self.calculated = True

    def __y_0(self, s):
        return sum([self.G(s - self.S_m0[i]) * self.u0[i] for i in range(self.M0)])

    def __y_G(self, s):
        return sum([self.G(s - self.S_mG[i]) * self.uG[i] for i in range(self.MG)])

    def __y_inf(self, s):
        return self.y(s)

    def my_y(self, s):
        if not self.calculated:
            self.__calculate()
        return self.__y_inf(s) + self.__y_0(s) + self.__y_G(s)

    def demo(self):
        print("launched")
        
        step = 0.1
        ptsX = int((self.x_max - self.x_min) / step) + 1
        ptsY = int((self.y_max - self.y_min) / step) + 1

        h_min = -10
        h_max = 10

        if self.dim == 2:
            fig, ax = plt.subplots(figsize=(16, 9), dpi=70)
        else:
            fig = plt.figure(figsize=(16, 9), dpi=70)
            ax = fig.add_subplot(111, projection='3d')

        X = np.arange(self.x_min, self.x_max + step, step)

        # formating
        font = 20
        pad = 20
        matplotlib.rcParams.update({'font.size': font})

        # observations

        start_viewX = [self.X_L0[i][0] for i in range(self.L0)]
        border_viewX = [self.X_LG[i][0] for i in range(self.LG)]

        if self.dim == 3:
            Y = np.arange(self.y_min, self.y_max + step, step)
            X, Y = np.meshgrid(X, Y)
            start_viewY = [self.X_L0[i][1] for i in range(self.L0)]
            border_viewY = [self.X_LG[i][1] for i in range(self.LG)]

        def animate(i):
            ax.clear()
            plt.title("t = {0}".format(i))
            if self.dim == 2:
                ax.set_xlabel('x', fontsize=font, labelpad=pad)
                ax.set_ylabel('y', fontsize=font, labelpad=pad)
                ax.set_xlim(self.x_min, self.x_max)
                ax.set_ylim(h_min, h_max)
                Z = np.array([self.my_y((X[j], i)) for j in range(ptsX)])
                line, = ax.plot(X, Z)
                plt.plot(start_viewX, self.Y_L0, 'ro', label="starting conditions")
                plt.plot(border_viewX, self.Y_LG, 'bo', label="border conditions")
                plt.grid()
                plt.legend()
                return line,
            else:
                ax.set_xlabel('x1', fontsize=font, labelpad=pad)
                ax.set_ylabel('x2', fontsize=font, labelpad=pad)
                ax.set_zlabel('y', fontsize=font, labelpad=pad)
                ax.set_xlim(self.x_min, self.x_max)
                ax.set_ylim(self.y_min, self.y_max)
                ax.set_zlim(h_min, h_max)
                # ax.view_init(azim=-130, elev=40)
                Z = np.array([[self.my_y((X[j][k], Y[j][k], i)) for k in range(ptsX)] for j in range(ptsY)])
                frame = ax.plot_surface(X, Y, Z, cmap=cm.twilight, alpha=0.3, linewidth=0, antialiased=False)
                plt.plot(start_viewX, start_viewY, self.Y_L0, 'ro', label="starting conditions")
                plt.plot(border_viewX, border_viewY,  self.Y_LG, 'bo', label="border conditions")
                # plt.grid(show=True)
                plt.legend()
                return frame

        pause = True

        def onClick(event):
            nonlocal pause
            if pause:
                ani.event_source.stop()
            else:
                ani.event_source.start()
            pause ^= True


        fig.canvas.mpl_connect('button_press_event', onClick)
        ani = animation.FuncAnimation(fig, animate, frames=self.time,
                                      interval=100, blit=False)

        # for saving video
        #  plt.rcParams['animation.ffmpeg_path'] = r'C:\Users\Ihor\Downloads\ffmpeg\ffmpeg-20181015-c27c7b4-win64-static\ffmpeg-20181015-c27c7b4-win64-static\bin\ffmpeg.exe'
        #  Writer = animation.writers['ffmpeg']
        #  writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
        #  ani.save('demo2.mp4', writer=writer)

        plt.show()


#if __name__ == "__main__":
    #model = Model(2, 1, 1, 100, -5, 5, -5, 5)
    #model.set_start_conditions([(1, 1, 0), (2, 2, 0), (5, 4, 0), (3, 3, 0), (4, 3, 0), (5, 4, 0)])
    #model.set_border_conditions([(0, 0, 2), (5, 4, 5), (1, -1, 3), (4, 5, 7)])
    #model.set_points_sm0([(1, 5, -1), (2, 4, -1), (3, 3, -1), (4, 2, -1), (5, 1, -1)])
    #model.set_points_smG([(5, 4, 0), (-5, 4, 0), (-5, -4, 0), (-5, 0, 0), (5, 0, 0)])
    #model.set_start_conditions([(1, 0), (2, 0), (3, 0), (4, 0), (-1, 0)])
    #model.set_border_conditions([(-5, 50), (5, 50)])
    #model.set_points_sm0([(1, -1), (2, -1), (3, -1), (4, -1), (5, -1)])
    #model.set_points_smG([(-5, 0), (5, 0)])
    
    #model.set_start_conditions([(1, 0)])
    #model.set_border_conditions([(-5, 50)])
    #model.demo()
