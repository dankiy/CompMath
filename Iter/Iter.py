import math
import numpy as np

def Seidel(A, b, eps):
    steps = 0
    n = len(A)
    x = [0.0 for i in range(n)]

    conv = False
    while not conv:
        newX = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * newX[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i+1, n))
            newX[i] = (b[i]-s1-s2) / A[i][i]

        conv = math.sqrt(sum((newX[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = newX

        steps += 1

    return x, steps

def Jacobi(A, b, eps):
    steps = 0
    n = len(A)
    tempX = [0.0 for i in range(n)]
    x = [4.0 for i in range(n)]
    norm = eps + 1

    while norm > eps:
        for i in range(n):
            tempX[i] = b[i]
            for j in range(n):
                if i != j:
                    tempX[i] -= A[i][j] * x[j]
            tempX[i] /= A[i][i]

        norm = math.fabs(x[0] - tempX[0])

        for j in range(n):
            if math.fabs(x[j]) - tempX[j] > norm:
                norm = math.fabs(x[j] - tempX[j])
            x[j] = tempX[j]

        steps += 1

    return x, steps