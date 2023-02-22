# Eva Fountain
# COT4500, Spring 2023
# Assignment 2

import math
import numpy as np

np.set_printoptions(precision=7, suppress=True, linewidth=100)


# ^ to have decimals correct

# Number 1
def nevilles_method(x_points, y_points, x):
    matrix = len(x_points)
    y = y_points.copy()

    for i in range(1, matrix):
        y[0:matrix - i] = ((x - x_points[i:matrix]) * y[0:matrix - i] + \
                           (x_points[0:matrix - i] - x) * y[1:matrix - i + 1]) / \
                          (x_points[0:matrix - i] - x_points[i:matrix])
    return y[0]


x_points = np.array([3.6, 3.8, 3.9])
y_points = np.array([1.675, 1.436, 1.318])
x = 3.7

print("Number 1: ")
print(nevilles_method(x_points, y_points, x))
print("\n")


# Number 2
def div_diff_table(x, y):
    size: int = len(x)
    matrix : np.array = np.zeros([2, 4])

    for i in range(1, size):
        for j in range(i, size):
            matrix[j][i] = (matrix[j+1][i-1] - matrix[j][i-1]) / \
                           (x[i+j] - x[j])
    return matrix


def approx_result(matrix, x_points, n):
    size = len(x_points) - 1
    polynomial_coef = matrix[size]
    for i in range(1, size + 1):
        polynomial_coef = matrix[size - i] + (n - x_points[size - i]) * polynomial_coef
    return polynomial_coef


x_points = [7.2, 7.4, 7.5, 7.6]
y_points = [23.5492, 25.3913, 26.8224, 27.4589]
divided_table = div_diff_table(x_points, y_points)
final_approx1 = approx_result(divided_table, x_points, y_points, 1)
final_approx2 = approx_result(divided_table, x_points, y_points, 2)
final_approx3 = approx_result(divided_table, x_points, y_points, 3)
print(final_approx1)
print(final_approx2)
print(final_approx3)

# Number 3 needs answer to 2

# Number 4

# Number 5
# a - matrix A
#def cublic_spline(x_points, y_points):

# b - Vector b

# c - Vector x


# Can't quite get this working
# Still learning Python
# :(