import LU
import numpy as np
from math import log, acos, cos, pi

#1. f(x) = 2*cos(2.5*x)*exp(x/3) + 4*sin(3.5*x)*exp(-3*x) + x
#   a = 1.5, b = 3.3, alpha = 1/3, beta = 0

np.set_printoptions(suppress = True)
def ACPI(f, a, b, eps, opt: bool, gauss = False):
    L = 2
    h1 = 1
    h2 = h1 / L
    h3 = h2 / L
    if opt:
        S1 = CPIh(f, a, b, h1, gauss)
        S2 = CPIh(f, a, b, h2, gauss)
        S3 = CPIh(f, a, b, h3, gauss)
        m = Atkin(S1, S2, S3, L)
        h1 = h1 * ( ( eps * (1 - L ** (-m)) / abs(S2 - S1) )  ** (1 / m) )
        h2 = h1 / L
        h3 = h2 / L
        print("hopt = " + str(h1))
    R = 2 * eps
    while R > eps:
        S1 = CPIh(f, a, b, h1, gauss)
        S2 = CPIh(f, a, b, h2, gauss)
        S3 = CPIh(f, a, b, h3, gauss)
        m = Atkin(S1, S2, S3, L)
        R = Richardson(S1, S2, L, m) #Richardson
        h1 = h2
        h2 = h3
        h3 = h3 / L

    result = S3

    return result

def Atkin(S1, S2, S3, L):
    m = -log((S3 - S2) / (S2 - S1)) / (log(L))
    return m

def Richardson(S1, S2, L, m):
    R = (S2 - S1) / (1 - L ** (-m))
    return R

def CPI(f, a, b, steps, gauss = False):
    PI = GPI if gauss else NPI
    h = (b - a) / steps
    intervals = [(a + h * i, a + h * (i + 1)) for i in range(steps)]
    result = sum([PI(f, x[0], x[1]) for x in intervals])

    return result

def CPIh(f, a, b, h, gauss = False):
    PI = GPI if gauss else NPI
    intervals = []
    i = 0
    while a + i * h < b:
        next = a + (i + 1) * h
        intervals.append((a + i * h, next if next < b else b))
        i += 1
    result = sum([PI(f, x[0], x[1]) for x in intervals])

    return result

def NPI(f, x0, x1, a = 1.5, b = 3.3):
    n = 3
    x = np.array([x0, (x0 + x1) / 2, x1])
    X = np.array([[xj ** s for xj in x] for s in range(n)])
    m = np.array([mu(x0, x1, s) for s in range(n)])
    A = np.linalg.solve(X, m)
    result = sum([A[j] * f(x[j]) for j in range(n)])

    return result

def GPI(f, x0, x1, a = 1.5, b = 3.3):
    n = 3
    m = np.array([mu(x0, x1, s) for s in range(2 * n)])
    mmu = np.array([-m[i] for i in range(n, 2 * n)])
    M = np.array([m[i:n+i] for i in range(n)])
    k = np.linalg.solve(M, mmu)
    x = np.array(Kardano(k))
    X = np.array([[xj ** s for xj in x] for s in range(n)])
    A = np.linalg.solve(X, m[:n])
    result = sum([A[j] * f(x[j]) for j in range(n)])

    return result

def Kardano(k):
    b = k[2]
    c = k[1]
    d = k[0]
    q = (b ** 2 - 3 * c) / 9
    r = (2 * b ** 3 - 9 * b * c + 27 * d) / 54
    s = q ** 3 - r ** 2
    phi = acos(r / (q ** (3 / 2))) / 3
    x1 = -2 * (q ** (1 / 2)) * cos(phi) - b / 3
    x2 = -2 * (q ** (1 / 2)) * cos(phi + 2 * pi / 3) - b / 3
    x3 = -2 * (q ** (1 / 2)) * cos(phi - 2 * pi / 3) - b / 3

    return x1, x2, x3

def mu(x0, x1, j, a = 1.5, b = 3.3):
    d = 1 / 3
    def __indef0(x):
        return ((x - a) ** (1 - d)) / (1 - d)
    def __indef1(x):
        return ((x - a) ** (1 - d)) / (d - 2) * (a - d * x + x) / (d - 1)
    def __indef2(x):
        return -((x - a) ** (1 - d)) * (2 * a * a - 3 * (d - 1) * x + (d * d - 3 * d + 2) * x * x) \
               / (d - 3) / (d - 2) / (d - 1)
    def __indef3(x):
        return ((x - a) ** (1 - d)) * (6 * a ** 3 - 6 * a ** 2 * (d - 1) * x +
                          3 * a * (d * d - 3 * d + 2) * x ** 2 -
                          (d * d * d - 6 * d * d + 11 * d - 6) * x ** 3) / (d - 4) / (d - 3) / (d - 2) / (d - 1)
    def __indef4(x):
        return -((x - a) ** (1 - d)) * (24 * a ** 4 - 24 * a ** 3 * (d - 1) * x +
                            12 * a * a * (d * d - 3 * d + 2) * x * x -
                            4 * a * (d * d * d - 6 * d * d + 11 * d - 6) * x * x * x +
                            (d * d * d * d - 10 * d * d * d + 35 * d * d - 50 * d + 24) *
                            x ** 4) / (d - 5) / (d - 4) / (d - 3) / (d - 2) / (d - 1)
    def __indef5(x):
        return ((x - a) ** (1 - d)) * (120 * a ** 5 - 120 * a ** 4 * (d - 1) * x +
                          60 * a ** 3 * (d * d - 3 * d + 2) * x * x -
                          20 * a * a * (d * d * d - 6 * d * d + 11 * d - 6) * x * x * x + 5 *
                          a *
                          (d ** 4 - 10 * d * d * d + 35 * d * d - 50 * d + 24) *
                          x ** 4 -
                          (d ** 5 - 15 * d ** 4 + 85 * d * d * d - 225 * d * d +
                           274 * d - 120) *
                          x ** 5) / (d - 6) / (d - 5) / (d - 4) / (d - 3) / (d - 2) / (d - 1)

    indef = [__indef0, __indef1, __indef2, __indef3, __indef4, __indef5]

    return indef[j](x1) - indef[j](x0)