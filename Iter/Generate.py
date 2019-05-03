import numpy as np
import math
import random

def Generate(n, q):
    matrix = np.random.rand(n, n)
    b = np.random.rand(n)
    for i in range(n):
        matrix[i][i] = 0
        for j in range(n):
            if i != j:
                matrix[i][i] += math.fabs(matrix[i][j])
        matrix[i][i] *= q
        #matrix[i][i] *= random.paretovariate(1)
    return matrix, b