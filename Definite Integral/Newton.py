def Newton(f, k, x0: float, eps: float = 1e-9, kmax: int = 1e3) -> float:
    x = x0
    x_prev = x0 + 2 * eps
    i = 0

    while abs(x - x_prev) >= eps and i < kmax:
        x = x - f(x, k) / der(f, k, x)
        x_prev = x
        i += i + 1

    return x

def der(func, k, point, eps: float = 1e-9):
    newPoint = point + eps
    der = (func(newPoint, k) - func(point, k)) / eps
    return der