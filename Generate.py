import numpy as np

def Generate(n):
    matrix = np.random.random(n,n)
    b = np.random.random(n,1)
    return matrix, b