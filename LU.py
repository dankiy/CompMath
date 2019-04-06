import numpy as np

class LU:
    def __init__(self, matrix, b):
        self.L = np.eye(len(matrix)).map(
            lambda i, j: [matrix[i, j] / matrix[i, j - 1] for j in range(1, len(matrix) - i)] for i in
            range(len(matrix)))
        self.b = np.array(matrix[:, 0].map(lambda i: i * b[i]))
        self.U = [[matrix[i, j](1 - self.L[i, j]) for i in range(0, len(matrix))] for j in range(0, len(matrix))]
    def __init__(self, matrix, b, x, y):
        matrix[[0, x]] = matrix[[x, 0]] #swapping rows
        matrix[:, 0], matrix[:, y] = matrix[:, y], matrix[:, 0].copy() #swapping columns
        self.L = np.eye(len(matrix)).map(
            lambda i, j: [matrix[i, j] / matrix[i, j - 1] for j in range(1, len(matrix) - i)] for i in
            range(len(matrix)))
        self.b = np.array(matrix[:, 0].map(lambda i: i * b[i]))
        self.U = [[matrix[i, j](1 - self.L[i, j]) for i in range(0, len(matrix))] for j in range(0, len(matrix))]
    def print(self):
        print(self.L)
        print(self.U)
        print(self.b)