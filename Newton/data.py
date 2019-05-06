import numpy as np
from math import sin, cos, sinh, cosh, exp, pow

def __func1(x: np.array) -> float:
    -(cos(x[0] * x[1]) - exp(-3 * x[2]) + x[3] * pow(x[4], 2) - x[5] - sinh(2 * x[7]) * x[8] + 2 * x[
        9] + 2.0004339741653854440)
def __func2(x: np.array) -> float:
    -(sin(x[0] * x[1]) + x[2] * x[8] * x[6] - exp(-x[9] + x[5]) + 3 * pow(x[4], 2) - x[5] * (
                x[7] + 1) + 10.886272036407019994)
def __func3(x: np.array) -> float:
    -(x[0] - x[1] + x[2] - x[3] + x[4] - x[5] + x[6] - x[7] + x[8] - x[9] - 3.1361904761904761904)
def __func4(x: np.array) -> float:
    -(2 * cos(-x[8] + x[3]) + x[4] / (x[2] + x[0]) - sin(x[1] * x[1]) + pow(cos(x[6] * x[9]), 2) - x[
        7] - 0.1707472705022304757)
def __func5(x: np.array) -> float:
    -(sin(x[4]) + 2 * x[7] * (x[2] + x[0]) - exp(-x[6] * (-x[9] + x[5])) + 2 * cos(x[1]) - 1 / (
                x[3] - x[8]) - 0.368589627310127786)
def __func6(x: np.array) -> float:
    -(exp(x[0] - x[3] - x[8]) + x[4] * x[4] / x[7] + 0.5 * cos(3 * x[9] * x[1]) - x[5] * x[2] + 2.049108601677187511)
def __func7(x: np.array) -> float:
    -x[1] * x[1] * x[1] * x[6] - (-sin(x[9] / x[4] + x[7]) + (x[0] - x[5]) * cos(x[3]) + x[2] - 0.738043007620279801)
def __func8(x: np.array) -> float:
    -(x[4] * pow(x[0] - 2 * x[5], 2) - 2 * sin(-x[8] + x[2]) + 1.5 * x[3] - exp(
        x[1] * x[6] + x[9]) + 3.566832198969380904)
def __func9(x: np.array) -> float:
    -(7 / x[5] + exp(x[4] + x[3]) - 2 * x[1] * x[7] * x[9] * x[6] + 3 * x[8] - 3 * x[0] - 8.439473450838325749)
def __func10(x: np.array) -> float:
    -(x[9] * x[0] + x[8] * x[1] - x[7] * x[2] + sin(x[3] + x[4] + x[5]) * x[6] - 0.7823809523809523809)

funcSystem = [__func1, __func2, __func3, __func4, __func5, __func6, __func7, __func8, __func9, __func10]

def getFuncSystem():
    return funcSystem

x1 = 0.5
x2 = 0.5
x3 = 1.5
x4 = -1.0
x5 = -0.5
x6 = 1.5
x7 = 0.5
x8 = -0.5
x9 = 1.5
x10 = -1.5

x = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10])

def getStartVector():
    return x
'''
cg = [][]

cg[0][0] = -sin(x1 * x2) * x2
cg[0][1] = -sin(x1 * x2) * x1
cg[0][2] = 3. * exp(- (3 * x3))
cg[0][3] = x5 * x5
cg[0][4] = 2 * x4 * x5
cg[0][5] = -1.
cg[0][6] = 0.
cg[0][7] = -2. * cosh( (2 * x8)) * x9
cg[0][8] = -sinh( (2 * x8))
cg[0][9] = 2.
cg[1][0] = cos(x1 * x2) * x2
cg[1][1] = cos(x1 * x2) * x1
cg[1][2] = x9 * x7
cg[1][3] = 0
cg[1][4] = 6 * x5
cg[1][5] = -exp(-x10 + x6) - x8 - 0.1e1
cg[1][6] = x3 * x9
cg[1][7] = -x6
cg[1][8] = x3 * x7
cg[1][9] = exp(-x10 + x6)
cg[2][0] = 1.
cg[2][1] = -1.
cg[2][2] = 1.
cg[2][3] = -1.
cg[2][4] = 1.
cg[2][5] = -1.
cg[2][6] = 1.
cg[2][7] = -1.
cg[2][8] = 1.
cg[2][9] = -1.
cg[3][0] = - x5 * pow( x3 + x1, -2.)
cg[3][1] = -2. * cos(x2 * x2) * x2
cg[3][2] = - x5 * pow( x3 + x1, -2.)
cg[3][3] = -2. * sin(-x9 + x4)
cg[3][4] = 1. / ( x3 + x1)
cg[3][5] = 0.
cg[3][6] = -2. * cos(x7 * x10) * sin(x7 * x10) * x10
cg[3][7] = -1.
cg[3][8] = 2. * sin(-x9 + x4)
cg[3][9] = -2. * cos(x7 * x10) * sin(x7 * x10) * x7
cg[4][0] = 2. * x8
cg[4][1] = -2. * sin(x2)
cg[4][2] = 2. * x8
cg[4][3] = pow(-x9 + x4, -2.)
cg[4][4] = cos(x5)
cg[4][5] = x7 * exp(-x7 * (-x10 + x6))
cg[4][6] = -(x10 - x6) * exp(-x7 * (-x10 + x6))
cg[4][7] = (2. * x3) + 2. * x1
cg[4][8] = -pow(-x9 + x4, -2.)
cg[4][9] = -x7 * exp(-x7 * (-x10 + x6))
cg[5][0] = exp(x1 - x4 - x9)
cg[5][1] = -3. / 2. * sin(3. * x10 * x2) * x10
cg[5][2] = -x6
cg[5][3] = -exp(x1 - x4 - x9)
cg[5][4] = 2. * x5 / x8
cg[5][5] = -x3
cg[5][6] = 0.
cg[5][7] = -x5 * x5 * pow( x8, (-2.))
cg[5][8] = -exp(x1 - x4 - x9)
cg[5][9] = -3. / 2. * sin(3. * x10 * x2) * x2
cg[6][0] = cos(x4)
cg[6][1] = 3. * x2 * x2 * x7
cg[6][2] = 1.
cg[6][3] = -(x1 - x6) * sin( x4)
cg[6][4] = cos(x10 / x5 + x8) * x10 * pow(x5, (-2.))
cg[6][5] = -cos(x4)
cg[6][6] = pow(x2, 3.)
cg[6][7] = -cos(x10 / x5 + x8)
cg[6][8] = 0.
cg[6][9] = -cos(x10 / x5 + x8) / x5
cg[7][0] = 2. * x5 * (x1 - 2. * x6)
cg[7][1] = -x7 * exp(x2 * x7 + x10)
cg[7][2] = -2. * cos(-x9 + x3)
cg[7][3] = 0.15e1
cg[7][4] = pow(x1 - 2. * x6, 2.)
cg[7][5] = -4. * x5 * (x1 - 2. * x6)
cg[7][6] = -x2 * exp(x2 * x7 + x10)
cg[7][7] = 0.
cg[7][8] = 2. * cos(-x9 + x3)
cg[7][9] = -exp(x2 * x7 + x10)
cg[8][0] = -3.
cg[8][1] = -2. * x8 * x10 * x7
cg[8][2] = 0.
cg[8][3] = exp(x5 + x4)
cg[8][4] = exp(x5 + x4)
cg[8][5] = -0.7e1 * pow(x6, -2.)
cg[8][6] = -2. * x2 * x8 * x10
cg[8][7] = -2. * x2 * x10 * x7
cg[8][8] = 3.
cg[8][9] = -2. * x2 * x8 * x7
cg[9][0] = x10
cg[9][1] = x9
cg[9][2] = -x8
cg[9][3] = cos(x4 + x5 + x6) * x7
cg[9][4] = cos(x4 + x5 + x6) * x7
cg[9][5] = cos(x4 + x5 + x6) * x7
cg[9][6] = sin(x4 + x5 + x6)
cg[9][7] = -x3
cg[9][8] = x2
cg[9][9] = x1

def getCG():
    return cg '''

