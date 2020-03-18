#!/usr/bin/python3

import numpy as np


# a, b = 3, 4
# for a in range(3, 999):
#     for b in range(1, 800):
#         c = np.sqrt(a*a + b*b)
#         if c == int(c):
#             if a+b+c == 1000:
#                 print(f'a: {a}')
#                 print(f'b: {b}')
#                 print(f'c: {c}')
#                 print(f'abc: {a*b*c}')


# 10 ###########################################

def is_prime(num: int):
    i = 3
    while i <= np.sqrt(num)+1:
        if num % i == 0:
            return 0
        i +=1
    return 1


sum = 2
for num in range(3, 2_000_000, 2):
    if is_prime(num):
        sum += num

print(f'sum: {sum}')