import LU
import numpy as np
from math import log

#9. f(x) = 3*cos(1.5*x)exp(x/4) + 4*sin(3.5*x)*exp(-3*x) + 4*x
#   a = 2.5, b = 3.3, alpha = 2/3, beta = 0

def ACPI(f, a, b, eps, opt: bool):
    L = 2
    h1 = 1
    h2 = h1 / L
    h3 = h2 / L
    if opt:
        S1 = CPIh(f, a, b, h1)
        S2 = CPIh(f, a, b, h2)
        S3 = CPIh(f, a, b, h3)
        m = Atkin(S1, S2, S3, L)
        h1 = h1 * ( ( eps * (1 - L ** (-m)) / (S2 - S1) )  ** (1 / m) )
        h2 = h1 / L
        h3 = h2 / L
        print(h1)
    R = 2 * eps
    while R > eps:
        S1 = CPIh(f, a, b, h1)
        S2 = CPIh(f, a, b, h2)
        S3 = CPIh(f, a, b, h3)
        print("value: " + str(S3))
        m = Atkin(S1, S2, S3, L)
        R = abs((S2 - S1) / (1 - L ** (-m)))
        print("R: " + str(R))
        h1 = h2
        h2 = h3
        h3 = h3 / L

    result = S3
    return result

def Atkin(S1, S2, S3, L):
    print((S3 - S2) / (S2 - S1))
    m = -log((S3 - S2) / (S2 - S1)) / (log(L))
    return m

def CPI(f, a, b, steps):
    h = (b - a) / steps
    intervals = [(a + h * i, a + h * (i + 1)) for i in range(steps)]
    result = sum([NPI(f, x[0], x[1]) for x in intervals])
    return result

def CPIh(f, a, b, h):
    intervals = []
    i = 0
    while a + i * h < b:
        next = a + (i + 1) * h
        intervals.append((a + i * h, next if next < b else b))
        i += 1
    result = sum([NPI(f, x[0], x[1]) for x in intervals])
    return result

def NPI(f, x0, x1, a = 2.5, b = 3.3):
    x = np.array([x0, (x0 + x1) / 2, x1])
    X = np.array([[xj ** s for xj in x] for s in range(len(x))])
    m = np.array([mu(x0, x1, j) for j in range(len(x))])
    luX = LU.LU(X, m)
    A = luX.solve()
    result = sum([A[j] * f(x[j]) for j in range(len(x))])
    return result

def mu(x0, x1, j):
    a = 2.5
    b = 3.3

    def __indef0(x: float) -> float:
        return 3 * ( (x - a) ** (1 / 3) )
    def __indef1(x: float) -> float:
        return (3 / 4) * ( (x - a) ** (1 / 3) ) * (3 * a + x)
    def __indef2(x: float) -> float:
       return (3 / 14) * ( (x - a) ** (1 / 3) ) * (9 * (a ** 2) + 3 * a * x + 2 * (x ** 2))
    def __indef3(x: float) -> float:
       return (3 / 140) * ( (x - a) ** (1 / 3) ) * \
              (81 * (a ** 3) + 27 * (a ** 2) * x + 18 * a * (x ** 2) + 14 * (x ** 3))
    def __indef4(x: float) -> float:
       return (3 / 455) * ( (x - a) ** (1 / 3) ) * \
              (243 * (a ** 4) + 81 * (a ** 3) * x + 54 * (a ** 2) * (x ** 2) + 42 * a * (x ** 3) + 35 * (x ** 4))
    def __indef5(x: float) -> float:
        return (3 / 1456) * ((x - a) ** (1 / 3)) * \
               (729 * (a ** 5) + 243 * (a ** 4) * x + 162 * (a ** 3) * (x ** 2) + 126 * (a ** 2) * (x ** 3)
                + 105 * a * (x ** 4) + 91 * (x ** 5))
    def __indef6(x: float) -> float:
        return (3 / 13832) * ((x - a) ** (1 / 3)) * \
               (6561 * (a ** 6) + 2187 * (a ** 5) * x + 1458 * (a ** 4) * (x ** 2) + 1134 * (a ** 3) * (x ** 3)
                + 945 * (a ** 2) * (x ** 4) + 819 * a * (x ** 5) + 728 * (x ** 6))

    indef = [__indef0, __indef1, __indef2, __indef3, __indef4, __indef5, __indef6]

    return indef[j](x1) - indef[j](x0)