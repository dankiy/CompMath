import numpy as np
import LU

def Newton(funcSystem, x0, k: int = 1, kmax: int = 1e3, eps: float = 1e-9, lim: int = 1e3):
    x = x0
    x_prev = x0 + [2 * eps for i in range(len(x0))]
    i = 0
    if k == -1:
        W = Jacobi(funcSystem, x)
    while max([abs(x[i] - x_prev[i]) for i in range(len(x))]) >= eps and i < lim:
        if k != -1 and i % k == 0 and i < kmax:
            W = Jacobi(funcSystem, x)
        x_prev = x
        f = np.array([funcSystem[i](x) for i in range(len(x))])
        b = np.array([0 for i in range(len(W))])
        luW = LU.LU(W, b)

        x = x - np.dot(luW.inverse(), f)
        #x = x - np.dot(np.linalg.inv(W),f)
        i += 1
    return x, i

def Jacobi(funcSystem, x0):
    n = len(funcSystem)
    jacobi = np.array([[der(funcSystem[i], x0, j) for j in range(n)] for i in range(n)])
    return jacobi

def der(func, point, index, eps: float = 1e-9):
    newPoint = point.copy()
    newPoint[index] += eps
    der = (func(newPoint) - func(point)) / eps
    return der