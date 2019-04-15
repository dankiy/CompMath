import numpy as np

class LU:

    def __init__(self, matrix, b):
        """
        self.L = np.eye(len(matrix)).map(
            lambda i, j: [matrix[i, j] / matrix[i, j - 1] for j in range(1, len(matrix) - i)] for i in
            range(len(matrix)))
        self.b = np.array(matrix[:, 0].map(lambda i: i * b[i]))
        self.U = [[matrix[i, j](1 - self.L[i, j]) for i in range(0, len(matrix))] for j in range(0, len(matrix))]
        """
        n = len(matrix)
        self.C = matrix
        for i in range(n):
            self.C, b = swap(self.C, b)
        if self.C[0][0] != 0:
            for j in range(i+1, n):
                self.C[j][i] /= self.C[i][i]
                for k in range(i+1, n):
                    self.C[j][k] -= self.C[j][i] * self.C[i][k]
        self.C -= np.eye(len(matrix))
        self.b = b

    def det(self):
        det = 1
        for i in range(len(self.C)): det *= self.C[i,i]
        return det

    def solve(self):
        solution = -self.b
        for i in range(2, len(solution)+1):
            for j in range(0, len(solution)):
                solution[len(solution)-i] -= solution[j]*np.tril(self.C)[j][i-2]
        return solution

    def show(self):
        print(np.tril(self.C))
        print()
        print(np.triu(self.C))
        print()
        print(self.b)
        print()

def swap(matrix, b):
    x = np.argmax(matrix[0])
    matrix[[0, x]] = matrix[[x, 0]]
    b[0], b[x] = b[x], b[0]
    return matrix, b
