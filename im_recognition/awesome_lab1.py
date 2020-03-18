#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
	data = np.loadtxt('task_lab1/f13.txt', delimiter=' ')

	T = 5.
	dt = .01
	time = np.arange(0, T + dt, dt)
	plt.rc('figure', figsize=(15, 15))
	plt.grid(True)
	plt.plot(time, data, color='k')
	plt.title('Initial data')
	plt.xlabel('time')
	plt.ylabel('data')
	plt.show()


	# building fourier transform
	n = data.shape[0]
	m = np.arange(n).reshape(n, 1).dot(np.arange(n).reshape(1, n))
	print(f'm {m.shape}')

	frequency = np.sqrt(
		(data.dot( np.sin(2. * np.pi * m / n)) / n) ** 2 +
		(data.dot( np.cos(2. * np.pi * m / n)) / n) ** 2
	)
	plt.plot(time, frequency, color='k')
	plt.title('Fourier transform')
	plt.xlabel('time')
	plt.ylabel('frequency')
	plt.show()


	biggest_value = []
	for i in range(3, n // 2):
		if np.max(frequency[i - 3:i + 4]) == frequency[i]:
			biggest_value.append(i)


	print(f'Highest peaks (i): {biggest_value}')
	main_frequency = biggest_value[0] / T
	print(f'Main frequency (value): {main_frequency}')


	components = np.vstack((time ** 3, time ** 2, time, np.sin(2. * np.pi * main_frequency * time), np.ones(n)))
	solution = np.linalg.solve(components.dot(components.T), data.dot(components.T))
	print(f'Solution (a_1, a_2, a_3, a_sin, a_0): {solution}')


	approximated_func = solution.dot(components)
	plt.grid(True)
	plt.plot(time, approximated_func, color='k')
	plt.xlabel('time')
	plt.ylabel('Founded approximated function')
	plt.title('Approximation')
	plt.show()

