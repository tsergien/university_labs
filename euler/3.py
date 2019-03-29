#!/usr/bin/python3

import numpy as np

def is_prime(n):
    i = 3
    max_divisor = np.sqrt(n)
    while i <= max_divisor:
        if n % i == 0:
            return 0
        i += 2
    return 1

# 600851475143
def count(n):
    first_div = int(np.sqrt(n)) + 1
    print(first_div)
    for i in range(first_div, 3, -2):
        if n % i == 0:
            print("i: ", i)
            if is_prime(i):
                print("max prime: ", i)
                break

import time
t0 = time.time() 
# count(13195)
count(600851475143)

print("Time: ", time.time() - t0)