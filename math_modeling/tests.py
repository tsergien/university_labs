#!/usr/bin/env python
import numpy as np
import lib


class Tester:
    @classmethod
    def __init__(cls):
        for attr in dir(cls):
            if 'test' in attr:
                getattr(cls, attr)()


class SolveLinearSystemTester(Tester):
    @staticmethod
    def test_diagonal():
        a = np.matrix([[1, 0], [0, 1]])
        b = np.array([[1], [2]])
        desired = np.array([[1], [2]])
        actual = lib.solve_linear_system(a, b)
        np.testing.assert_almost_equal(actual, desired)

    @staticmethod
    def test_antidiagonal():
        a = np.matrix([[0, 1], [1, 0]])
        b = np.array([[1], [2]])
        desired = np.array([[2], [1]])
        actual = lib.solve_linear_system(a, b)
        np.testing.assert_almost_equal(actual, desired)

    @staticmethod
    def test_pseudo():
        a = np.matrix([[1, 2], [1, 3], [1, 5]])
        b = np.array([[1], [2], [3]])
        desired = np.array([[-1/7], [9/14]])
        actual = lib.solve_linear_system(a, b)
        np.testing.assert_almost_equal(actual, desired)


class SolveSummedLinearSystemTester(Tester):
    @staticmethod
    def test_two_easy():
        as_list = [
            np.matrix([[1, 0], [0, 1], [0, 0], [0, 0]]),
            np.matrix([[0, 0], [0, 0], [1, 0], [0, 1]]),
        ]

        b = np.array([[1], [2], [3], [4]])
        desired = [np.array([[1], [2]]), np.array([[3], [4]])]
        actual = lib.solve_summed_linear_system(as_list, b)
        for actual_i, desired_i in zip(actual, desired):
            np.testing.assert_almost_equal(actual_i, desired_i)

    @staticmethod
    def test_two_hard():
        as_list = [np.matrix([[1, 2], [3, 4]]), np.matrix([[1, 2], [1, 3]])]
        b = np.array([[5], [7]])
        desired = [np.array([[-0.423077], [0.692308]]), np.array([[1.115385], [1.461538]])]
        actual = lib.solve_summed_linear_system(as_list, b)
        for actual_i, desired_i in zip(actual, desired):
            np.testing.assert_almost_equal(actual_i, desired_i, 6)

    @staticmethod
    def test_two_pseudo():
        as_list = [
            np.matrix([[1, 0], [1, 1], [0, 1], [0, 0], [0, 0]]),
            np.matrix([[0, 0], [0, 0], [1, 0], [1, 1], [0, 1]]),
        ]

        b = np.array([[5], [8], [13], [21], [34]])
        desired = [np.array([[0.4], [12.2]]), np.array([[-3.8], [29.4]])]
        actual = lib.solve_summed_linear_system(as_list, b)
        for actual_i, desired_i in zip(actual, desired):
            np.testing.assert_almost_equal(actual_i, desired_i)


class SolveTimeSummedLinearSystemTester(Tester):
    @staticmethod
    def test_two_easy():
        t = [0.0, 1.0]

        def a(t_i: float) -> np.matrix:
            return {
                0.0: np.matrix([[1, 0], [0, 1], [0, 0], [0, 0]]),
                1.0: np.matrix([[0, 0], [0, 0], [1, 0], [0, 1]]),
            }[t_i]

        b = np.array([[1], [2], [3], [4]])
        desired = [np.array([[1], [2]]), np.array([[3], [4]])]
        actual = lib.solve_time_summed_linear_system(a, b, t)
        for actual_i, desired_i in zip(actual, desired):
            np.testing.assert_almost_equal(actual_i, desired_i)

    @staticmethod
    def test_two_hard():
        t = [0.0, 1.0]

        def a(t_i: float) -> np.matrix:
            return {
                0.0: np.matrix([[1, 2], [3, 4]]),
                1.0: np.matrix([[1, 2], [1, 3]]),
            }[t_i]

        b = np.array([[5], [7]])
        desired = [np.array([[-0.423077], [0.692308]]), np.array([[1.115385], [1.461538]])]
        actual = lib.solve_time_summed_linear_system(a, b, t)
        for actual_i, desired_i in zip(actual, desired):
            np.testing.assert_almost_equal(actual_i, desired_i, 6)

    @staticmethod
    def test_two_pseudo():
        t = [0.0, 1.0]

        def a(t_i: float) -> np.matrix:
            return {
                0.0: np.matrix([[1, 0], [1, 1], [0, 1], [0, 0], [0, 0]]),
                1.0: np.matrix([[0, 0], [0, 0], [1, 0], [1, 1], [0, 1]]),
            }[t_i]

        b = np.array([[5], [8], [13], [21], [34]])
        desired = [np.array([[0.4], [12.2]]), np.array([[-3.8], [29.4]])]
        actual = lib.solve_time_summed_linear_system(a, b, t)
        for actual_i, desired_i in zip(actual, desired):
            np.testing.assert_almost_equal(actual_i, desired_i)


class SolveDistributedLinearSystemTester(Tester):
    @staticmethod
    def test_two_easy():
        as_list = [
            np.matrix([[1, 0], [0, 1]]),
            np.matrix([[1, 0], [0, 1]]),
        ]

        bs_list = [
            np.array([[2], [3]]),
            np.array([[2], [3]]),
        ]

        desired = np.array([[2], [3]])
        actual = lib.solve_distributed_linear_system(as_list, bs_list)
        np.testing.assert_almost_equal(actual, desired)

    @staticmethod
    def test_two_hard():
        as_list = [
            np.matrix([[1, 0], [0, 1]]),
            np.matrix([[1, 2], [3, 4]]),
        ]

        bs_list = [
            np.array([[2], [3]]),
            np.array([[8], [18]]),
        ]

        desired = np.array([[2], [3]])
        actual = lib.solve_distributed_linear_system(as_list, bs_list)
        np.testing.assert_almost_equal(actual, desired)

    @staticmethod
    def test_two_pseudo():
        as_list = [
            np.matrix([[1, 0], [0, 1]]),
            np.matrix([[0, 1], [1, 0]]),
        ]

        bs_list = [
            np.array([[2], [3]]),
            np.array([[5], [8]]),
        ]

        desired = np.array([[5], [4]])
        actual = lib.solve_distributed_linear_system(as_list, bs_list)
        np.testing.assert_almost_equal(actual, desired)


class SolveTimeDistributedLinearSystemTester(Tester):
    @staticmethod
    def test_two_easy():
        t = [0.0, 1.0]

        def a(t_i: float) -> np.matrix:
            return {
                0.0: np.matrix([[1, 0], [0, 1]]),
                1.0: np.matrix([[1, 0], [0, 1]]),
            }[t_i]

        def b(t_i: float) -> np.array:
            return {
                0.0: np.array([[2], [3]]),
                1.0: np.array([[2], [3]]),
            }[t_i]

        desired = np.array([[2], [3]])
        actual = lib.solve_time_distributed_linear_system(a, b, t)
        np.testing.assert_almost_equal(actual, desired)

    @staticmethod
    def test_two_hard():
        t = [0.0, 1.0]

        def a(t_i: float) -> np.matrix:
            return {
                0.0: np.matrix([[1, 0], [0, 1]]),
                1.0: np.matrix([[1, 2], [3, 4]]),
            }[t_i]

        def b(t_i: float) -> np.array:
            return {
                0.0: np.array([[2], [3]]),
                1.0: np.array([[8], [18]]),
            }[t_i]

        desired = np.array([[2], [3]])
        actual = lib.solve_time_distributed_linear_system(a, b, t)
        np.testing.assert_almost_equal(actual, desired)

    @staticmethod
    def test_two_pseudo():
        t = [0.0, 1.0]

        def a(t_i: float) -> np.matrix:
            return {
                0.0: np.matrix([[1, 0], [0, 1]]),
                1.0: np.matrix([[0, 1], [1, 0]]),
            }[t_i]

        def b(t_i: float) -> np.array:
            return {
                0.0: np.array([[2], [3]]),
                1.0: np.array([[5], [8]]),
            }[t_i]

        desired = np.array([[5], [4]])
        actual = lib.solve_time_distributed_linear_system(a, b, t)
        np.testing.assert_almost_equal(actual, desired)


class SolveIntegralLinearSystemTester(Tester):
    @staticmethod
    def test_simple():
        def a(t: float) -> np.matrix:
            return np.matrix([[t, 2 * t], [3 * t, 4 * t]])

        b = np.array([[1], [2]])
        T = 1.0

        def desired(t: float) -> np.matrix:
            return np.matrix([[0], [1.5 * t]])

        actual = lib.solve_integral_linear_system(a, b, T)
        for t in np.linspace(0.0, 1.0, 101):
            np.testing.assert_almost_equal(actual(t), desired(t))


class SolveFunctionalLinearSystemTester(Tester):
    @staticmethod
    def test_simple():
        def a(t: float) -> np.matrix:
            return np.matrix([[t, 2 * t], [3 * t, 4 * t]])

        def b(t: float) -> np.matrix:
            return np.matrix([[t], [2 * t]])

        T = 1.0
        desired = np.array([[0], [0.5]])
        actual = lib.solve_functional_linear_system(a, b, T)
        np.testing.assert_almost_equal(actual, desired)


if __name__ == "__main__":
    SolveLinearSystemTester()
    SolveSummedLinearSystemTester()
    SolveTimeSummedLinearSystemTester()
    SolveDistributedLinearSystemTester()
    SolveTimeDistributedLinearSystemTester()
    SolveIntegralLinearSystemTester()
    SolveFunctionalLinearSystemTester()
