#!/usr/bin/env python3

import numpy as np


def fill_distances(P, Q):
    distances = np.zeros((P.shape[0], Q.shape[0]))

    for i in range(P.shape[0]):
        for j in range(Q.shape[0]):
            distances[i,j] = np.sqrt((P[i][0]- Q[j][0])**2 + (P[i][1]- Q[j][1])**2)
    return distances


def NewtonGauss(P, distances):
    unknown_dots_list = []
    known_dots_len = distances.shape[0]
    unknown_dots_len = distances.shape[1]
    for i in range(unknown_dots_len):
        J = np.zeros((known_dots_len,2))
        F = np.zeros(known_dots_len)
        dot = np.random.rand(2)

        count = 0
        while count < 100:
            for j in range(known_dots_len):
                F[j] = (dot[0] - P[j,0])**2 + (dot[1]-P[j,1])**2 - distances[j, i]**2
                J[j] = [ 2*dot[0]-2*P[j,0], 2*dot[1] - 2*P[j,1] ]

            dot = dot - np.dot( np.dot( np.linalg.inv( np.dot(np.transpose(J), J)) , np.transpose(J) ), F )
            count += 1
            
        unknown_dots_list.append(dot)
    return unknown_dots_list


def LevenbergMarquardt(P, distances, lambd=1):
    '''
    parameters:
        P - set of known dots (N)
        distances - matrix NxM (where M len of unknown dots)
        lambd=1 - damping factor
    '''
    unknown_dots_list = []
    known_dots_len = distances.shape[0]
    unknown_dots_len = distances.shape[1]
    
    for i in range(unknown_dots_len):
        J = np.zeros((known_dots_len,2))
        F = np.zeros(known_dots_len)
        dot = np.random.rand(2)
        
        count = 0
        while count < 100:
            for j in range(known_dots_len):
                F[j] = (dot[0] - P[j,0])**2 + (dot[1]-P[j,1])**2 - distances[j, i]**2
                J[j] = [ 2*dot[0]-2*P[j,0], 2*dot[1] - 2*P[j,1] ]

            JTJ = np.dot(np.transpose(J), J)
            # dot = dot - np.dot( np.dot( np.linalg.inv( JTJ + lambd*np.diag(JTJ)) , np.transpose(J) ), F )
            dot = dot - np.dot( np.dot( np.linalg.inv( np.dot(np.transpose(J), J) + lambd*np.eye(2)) , np.transpose(J) ), F )
            count += 1
            
        unknown_dots_list.append(dot)
    return unknown_dots_list
    


if __name__ == "__main__":
    np.random.seed(777)
    N = 10
    M = 5
    P_points = np.random.rand(N,2) * 10
    Q_points = np.random.rand(M,2) * 10
    distances = fill_distances(P_points, Q_points) 
    distances += np.random.rand(N, M) / 10
    print(f'Known points: {P_points}')
    print(f'Unknown points: {Q_points}')
    print(f'Distances: {distances}')

    # result = NewtonGauss(P_points, distances)
    # print(f'\nNewton Gauss diff: {result - Q_points}')
    result_LM = LevenbergMarquardt(P_points, distances)
    print(f'\nLevenberg-Marquardt diff: {result_LM - Q_points}')

    