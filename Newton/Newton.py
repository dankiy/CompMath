def Newton(funcSystem, x0, eps: float = 1e-9, kmax: int = 1e3):
    x = x0
    x_prev = x0 + 2 * eps
    i = 0

    while max([abs(x[i] - x_prev[i]) for i in range(len(x))]) >= eps and i < kmax:
        #x = TODO
        x_prev = x
        i += 1

    return x, i

def Jacobi(funcSystem, x0):
    n = len(funcSystem)
    jacobi = [[der(funcSystem[i], x0, j) for j in range(n)] for i in range(n)]
    return jacobi

def der(func, point, index, eps: float = 1e-9):
    newPoint = point
    newPoint[index] += eps
    der = (func(newPoint) - func(point)) / eps
    return der