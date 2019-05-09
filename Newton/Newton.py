import numpy as np

def Newton(funcSystem, x0, k: int = 0, eps: float = 1e-9, lim: int = 1e3):
    x = x0
    x_prev = x0 + [2 * eps for i in range(len(x0))]
    i = 0
    if k == 0:
        while max([abs(x[i] - x_prev[i]) for i in range(len(x))]) >= eps and i < lim:
            W = Jacobi(funcSystem, x)
            x_prev = x
            f = np.array([funcSystem[i](x) for i in range(len(x))])
            x = x - np.dot(np.linalg.inv(W),f)
            i += 1

    else:
        pass
        ##TODO
    return x, i

def Jacobi(funcSystem, x0):
    n = len(funcSystem)
    jacobi = [[der(funcSystem[i], x0, j) for j in range(n)] for i in range(n)]
    return jacobi

def der(func, point, index, eps: float = 1e-9):
    newPoint = point.copy()
    newPoint[index] += eps
    der = (func(newPoint) - func(point)) / eps
    return der