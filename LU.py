import numpy as np
import math

class LU:

    def __init__(self, matrix, b):
        C = matrix.copy()
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
        y = self.b.copy()
        for i in range(1, len(y)):
            for j in range(i):
                y[i] -= y[j]*(np.tril(self.C,-1)+np.eye(len(self.C)))[i][j]
        x = y.copy()
        x[len(y)-1] /= np.triu(self.C)[len(y)-1][len(y)-1]
        for i in range(len(y)-2, -1, -1):
            for j in range(len(y)-1, i, -1):
                x[i] -= x[j]*(np.triu(self.C))[i][j]
            x[i] /= np.triu(self.C)[i][i]
        return x

    def inverse(self):
        LU = np.dot(np.tril(self.C,-1) + np.eye(len(self.C)), np.triu(self.C))
        inversion = []
        for i in range(len(LU)):
            b = [0 for k in range(len(LU))]
            b[i] = 1
            inversion.append(np.linalg.solve(LU, b))
        inversion = np.transpose(inversion)
        return inversion

    def cond(self):
        LU = np.dot(np.tril(self.C, 1) + np.eye(len(self.C)), np.triu(self.C))
        inversion = self.inverse()
        condition = np.linalg.norm(inversion) * np.linalg.norm(LU)
        return condition

    def show(self):
        print("L: ")
        print(np.tril(self.C,-1)+np.eye(len(self.C)))
        print("U: ")
        print(np.triu(self.C))
        print("P: ")
        print(self.P)
        print("b: ")
        print(self.b)
        print()
