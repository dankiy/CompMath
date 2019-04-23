import numpy as np

def Generate(n):
    matrix = np.random.rand(n,n)
    b = np.random.rand(n)
    return matrix, b