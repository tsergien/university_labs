#!/usr/bin/env python
import scipy.integrate as integrate
import typing as tp
import numpy as np


# section 1 subsection 1 problem 1
def solve_linear_system(a: np.matrix, b: np.array) -> np.array:
    """
    :param a: m times n real matrix
    :param b: m-dimensional real vector
    :return: n-dimensional real vector x,
        least squares solution to A x = b.
    """
    return np.linalg.pinv(a) * b


# section 1 subsection 2 problem 1
def solve_summed_linear_system(as_list: tp.List[np.matrix], b: np.array) -> tp.List[np.array]:
    """
    :param as_list: list of length N, consisting of m times n real matrixes A_i
    :param b: m-dimensional real vector
    :return: list x of length N, consisting of n-dimensional real vectors x_i,
        least squares solution to sum(A_i x_i for i in range(N)) = b.
    """
    p_1 = sum(a_i * a_i.T for a_i in as_list)
    return [a_i.T * np.linalg.pinv(p_1) * b for a_i in as_list]


# section 1 subsection 2 problem 2
def solve_time_summed_linear_system(a: tp.Callable[[float], np.matrix], b: np.array,
                                    t: tp.List[float]) -> tp.List[np.array]:
    """
    :param a: matrix-valued function of time.
        Maps t_i to m times n real matrix A(t_i)
    :param b: m-dimensional real vector
    :param t: N time moments, t_i
    :return: list x of length N, consisting of n-dimensional real vectors x(t_i),
        least squares solution to sum(A(t_i) x(t_i) for i in range(N)) = b.
    """
    as_list = [a(t_i) for t_i in t]
    return solve_summed_linear_system(as_list, b)


# section 1 subsection 3 problem 1
def solve_distributed_linear_system(as_list: tp.List[np.matrix],
                                    bs_list: tp.List[np.array]) -> np.array:
    """
    :param as_list: list of length N, consisting of m times n real matrixes A_i
    :param bs_list: list of length N, consisting of m-dimensional real vectors b_i
    :return: n-dimensional real vector x,
        least squares solution to A_i x = b_i, for i in range(N).
    """
    a_b = sum(a_i.T * b_i for a_i, b_i in zip(as_list, bs_list))
    p_2 = sum(a_i.T * a_i for a_i in as_list)
    return np.linalg.pinv(p_2) * a_b


# section 1 subsection 3 problem 2
def solve_time_distributed_linear_system(a: tp.Callable[[float], np.matrix],
                                         b: tp.Callable[[float], np.array],
                                         t: tp.List[float]) -> np.array:
    """
    :param a: matrix-valued function of time.
        Maps t_i to m times n real matrix A(t_i)
    :param b: vector-valued function of time.
        Maps t_i to m-dimensional real vector b(t_i)
    :param t: N time moments, t_i
    :return: n-dimensional real vector x,
        least squares solution to A(t_i) x = b(t_i), for i in range(N).
    """
    as_list = [a(t_i) for t_i in t]
    bs_list = [b(t_i) for t_i in t]
    return solve_distributed_linear_system(as_list, bs_list)


# section 1 subsection 4 problem 1
def solve_integral_linear_system(a: tp.Callable[[float], np.matrix], b: np.array,
                                 T: float) -> tp.Callable[[float], np.array]:
    """
    :param a: matrix-valued function of time.
        Maps t to m times n real matrix A(t)
    :param b: m-dimensional real vector
    :param T: end time
    :return: vector-valued function of time.
        Maps t to n-dimensional real vector x(t),
        least squares solution to int(A(t) x(t) for t in range(T)).
    """
    m, _ = (a(0) * a(0).T).shape

    p_1 = np.matrix([
        [
            integrate.quad(lambda t: (a(t) * a(t).T)[i, j], 0, T)[0] for j in range(m)
        ] for i in range(m)
    ])

    def x(t: float) -> np.array:
        return a(t).T * np.linalg.pinv(p_1) * b

    return x


# section 1 subsection 4 problem 2
def solve_functional_linear_system(a: tp.Callable[[float], np.matrix],
                                   b: tp.Callable[[float], np.array],
                                   T: float) -> np.array:
    """
    :param a: matrix-valued function of time.
        Maps t to m times n real matrix A(t)
    :param b: vector-valued function of time.
        Maps t to m-dimensional real vector b(t)
    :param T: end time
    :return: n-dimensional real vector x,
        least squares solution to A(t) x = b(t).
    """
    n, _ = (a(0).T * b(0)).shape

    a_b = np.array([
        [
            integrate.quad(lambda t: (a(t).T * b(t))[i], 0, T)[0]
        ] for i in range(n)
    ])

    p_2 = np.matrix([
        [
            integrate.quad(lambda t: (a(t).T * a(t))[i, j], 0, T)[0] for j in range(n)
        ] for i in range(n)
    ])

    return np.linalg.pinv(p_2) * a_b
