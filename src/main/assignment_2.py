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
       y[0:matrix - i] = ((x - x_points[i:matrix])*y[0:matrix-i] + \
                          (x_points[0:matrix-i] - x)*y[1:matrix-i+1])/ \
                         (x_points[0:matrix-i] - x_points[i:matrix])
    return y[0]

x_points = np.array([3.6, 3.8, 3.9])
y_points = np.array([1.675, 1.436, 1.318])
x = 3.7

print("Number 1: ")
print(nevilles_method(x_points, y_points, x))
print("\n")

# Number 2
def apply_div_dif(x_points, y_points):





# Number 3


# Number 4
def apply_div_dif(x_points, y_points):
    size = len(x_points)
    x_points.astype(float)
    y_points.astype(float)
    y = y_points.copy()
    array = []

    for i in range(size):
        array.append(y[i])

    for i in range(1, size):
        for j in range(size-1, i-1, -1):
            array[i] = float(array[j]-array[i-1])/float(x[j]-x[i-j])
    return np.array(array)


def hermite_interpolation():
    x_points = []
    y_points = []
    slopes = []

    num_of_points = len(x_points)
    matrix = np.zeros((3, 3))
    for x in range(??):
        break

    for x in range(??):
        break

    filled_matrix = apply_div_dif(matrix)
    print(filled_matrix)

hermite_interpolation()
