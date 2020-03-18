#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd

from nuages import LevenbergMarquardt


def rssi_to_m(rssi):
    Ptx = 18.5
    n = 2.6
    return np.power(10, (Ptx - rssi) / (np.power(10, n)))


def get_distances(df: pd.DataFrame, N):
    distances = np.zeros((N, df.shape[0]))
    num_df = df.select_dtypes(['int16', 'int32', 'int64', 'float16', 'float32', 'float64'])

    for row in range(N):
        for col in range(num_df.shape[0]):
            rssi = num_df.iloc[col, row]
            distances[row][col] = rssi_to_m(rssi)
            # print(f'dist = {distances[row][col]}, rssi = {rssi}')
    return distances


if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1], sep=",")
    df = df.sort_values(by='date', ascending=True)
    print(df[:10])
    
    # known dots P 
    N = 13
    P = np.array([[4.5, 8.6], [10, 4], [14, 4], [18.5, 4], [10, 7], [14, 7], [18.5, 7], [10, 10],\
        [4, 15], [10, 15.4], [14, 15.4], [17.8, 15.4], [22, 15.4]])
    
    print(f'-200 ->  {rssi_to_m(-200)}')
    print(f'-75  -> {rssi_to_m(-75)}')
    print(f'-50  -> {rssi_to_m(-50)}')
    dist = get_distances(df, N)
    Q = LevenbergMarquardt(P, dist)
    print(f'\nUsers locations : {Q[:20]}')