import random
import numpy
import math

#particle swarm oprimization

a = -10
b = 10
particles_amount = 50
dim = 3
w = 2
b_lo = -5
b_up = 5
A = 10
# criteria: iteration amount or best not changing
def criteria(particles):
    return True

def f(X, A):
    return A + sum([x ** 2 + A * math.cos(2 * math.pi * x) for x in X])

def particle_optimization():
    zeros_array = numpy.zeros( (particles_amount, dim) )
    particles = zeros_array
    next_pos = numpy.zeros((dim, 1))
    best_pos = zeros_array
    velocity = zeros_array
    gbest = zeros_array
    # init starting position
    for i in range(particles_amount):
        for k in range(dim):
            particles[i][k] = random.randint(b_lo, b_up)
        best_pos[i] = particles[i]
        if f(particles[i], A) > f(gbest[i], A):
            gbest[i] = particles[i]
        velocity[i] = (random.random(), random.random(), random.random())
    print(particles)
    while not criteria(particles):
        for i in range(particles_amount):
            for j in range(dim):
                rp = random.random()# rp and rg from[0;1]
                rg = random.random()
                velocity[i][j] = w * velocity[i][j] + rp * (best_pos[i][j] - particles[i][j]) * random.random() + \
                    rg * (gbest[i][j] - particles[i][j]) * random.random()
            next_pos[i] = particles[i] + velocity[i]
            if f(next_pos[i][j], A) < f(particles[i], A):
                particles[i] = next_pos[i]
                if f(particles[i], A) < f(gbest[i], A):
                    gbest[i] = particles[i] 


if __name__ == "__main__":
    particle_optimization()