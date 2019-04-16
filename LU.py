import numpy as np
import math

class LU:

    def __init__(self, C, b):
        n = len(C)
        P = np.eye(n)
        for i in range(n):
            pivotValue = 0
            pivot = -1
            for row in range(i, n):
                if (math.fabs(C[row][i]) > pivotValue):
                    pivotValue = math.fabs(C[row][i])
                    pivot = row
            if pivotValue != 0:
                C[[i, pivot]] = C[[pivot, i]]
                P[[i, pivot]] = P[[pivot, i]]
                b[i], b[pivot] = b[pivot], b[i]
                for j in range(i+1, n):
                    C[j][i] /= C[i][i]
                    for k in range(i+1, n):
                        C[j][k] -= C[j][i] * C[i][k]

        self.C = C
        self.P = P
        self.b = b

    def det(self):
        det = 1
        for i in range(len(self.C)): det *= self.C[i,i]
        return det

    def solve(self):
        solution = -self.b
        for i in range(2, len(solution)+1):
            for j in range(0, len(solution)):
                solution[len(solution)-i] -= solution[j]*(np.tril(self.C,-1)+np.eye(len(self.C)))[j][i-2]
        return solution

    def show(self):
        print(np.tril(self.C,-1)+np.eye(len(self.C)))
        print()
        print(np.triu(self.C))
        print()
        print(self.P)
        print()
        print(self.b)
        print()

    def cond(self):
        x = self.solve()


def swap(matrix, P, b, i):
    n = len(matrix)
    x = np.argmax([math.fabs(matrix[row][i]) for row in range(i, n)])
    matrix[[0, x]] = matrix[[x, 0]]
    P[[0, x]] = P[[x, 0]]
    b[0], b[x] = b[x], b[0]
    return matrix, P, b
