# particle swarm optimization

from random import random, randint, seed, Random
import numpy
from copy import copy
import math
import time

particles_amount = 50
dim = 4
w = 0.729
c1 = 1.49445
c2 = 1.49445
b_lo = -5.12
b_up = 5.12
iterations = 500

# -----> rastrigin function
def f(X):
    n = len(X)
    res = 0
    for i in range(n):
        res += X[i] * X[i] - 10 * math.cos(2 * math.pi * X[i]) + 10
    return res

# -----> sphere function
# def f(X):
#     n = len(X)
#     r = 0
#     for i in range(n):
#         r += X[i] * X[i]
#     return r

# -----> rosenbroke function
# def f(X):
#     n = len(X)
#     r = 0
#     for i in range(n-1):
#         r += 100 * (X[i+1] - X[i]*X[i])**2 + (X[i] - 1)**2
#     return r

# -----> ekli function
# def f(X):
#     res = -20 * math.exp(-0.2 * math.sqrt(X[0]**2 + X[1]**2)) - \
#         math.exp(0.5 * ( math.cos(2*math.pi*X[0]) + math.cos(2*math.pi*X[1]) ) ) + \
#             math.e + 20
#     return res

class Particle():
    def __init__(self, my_seed):
        self.rndm = Random(my_seed)
        self.position = [0.0 for i in range(dim)]
        self.velocity = [0.0 for i in range(dim)]

        for k in range(dim):
            self.position[k] = (b_up - b_lo) * self.rndm.random() + b_lo
            self.velocity[k] = (b_up - b_lo) * self.rndm.random() + b_lo
        self.my_best_pos = copy(self.position)


def particle_optimization():
    rndm = Random(0)
    swarm = [Particle(i) for i in range(particles_amount)]  
    gbest = copy(swarm[0].position)
    for i in range(particles_amount):
        if f(swarm[i].position) < f(gbest):
            gbest = copy(swarm[i].position)

    t1 = time.time()
    for epoch in range(0, iterations):
        if epoch % 20 == 0:
            print("Fitness function value: " + str(f(gbest)))
        for i in range(particles_amount):
            for j in range(dim):
                rp = rndm.random()
                rg = rndm.random()
                swarm[i].velocity[j] = w * swarm[i].velocity[j] + \
                    c1* rp * (swarm[i].my_best_pos[j] - swarm[i].position[j]) + \
                    c2 * rg * (gbest[j] - swarm[i].position[j])

            for d in range(dim):
                swarm[i].position[d] += swarm[i].velocity[d]
                if swarm[i].position[d] < b_lo:
                    swarm[i].position[d] = b_lo
                elif swarm[i].position[d] > b_up:
                    swarm[i].position[d] = b_up
            if f(swarm[i].position) < f(swarm[i].my_best_pos):
                print("new best position----> " + str(swarm[i].position))
                swarm[i].my_best_pos = copy(swarm[i].position)
                if f(swarm[i].my_best_pos) < f(gbest):
                    gbest = copy(swarm[i].my_best_pos)
                    print("New global best pos: " + str(gbest))
    print("\033[1;32m Time: \033[0;0m" + str(time.time() - t1))
    return gbest


n_round = 2
if __name__ == "__main__":
    print("Particle swarm optimization")
    res = particle_optimization()
    # for i in range(dim):
    #     res[i] = round(res[i], n_round)
    print("\033[1;32m Result:  \033[0;0m" + str(res))
    print("\033[1;32m Fitness in  \033[0;0m" + str(res) + " = " + str(f(res)) )
