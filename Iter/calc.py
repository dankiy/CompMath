import Iter
import Generate
import numpy as np

np.set_printoptions(suppress = True)
matrix, b = Generate.Generate(5, 4)
eps = 0.000001
print(" matrix:")
print(matrix)
print(" b:")
print(b)
print("\n Jacobi")
x, steps = Iter.Jacobi(matrix, b, eps)
print(x)
print(steps)
print("\n Seidel:")
x, steps = Iter.Seidel(matrix, b, eps)
print(x)
print(steps)
