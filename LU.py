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

    def det(self):
        det = 1
        for i in range(len(self.U)): det *= self.U[i,i]
        return det

    def solve(self):
        solution = -self.b
        for i in range(2, len(solution)+1):
            for j in range(0, len(solution)):
                solution[len(solution)-i] -= solution[j]*self.L[j][i-2]
        return solution

    def show(self):
        print(self.L)
        print(self.U)
        print(self.b)
