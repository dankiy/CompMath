import Iter
import Generate
import numpy as np

np.set_printoptions(suppress = True)
matrix, b = Generate.Generate(5, 1.2)
eps = 0.000001
print(" matrix:")
print(matrix)
print(" b:")
print(b)
acc = np.linalg.solve(matrix, b)
print("\n numpy.linalg.solve: ")
print(acc)
print("\n Jacobi")
x, steps = Iter.Jacobi(matrix, b, eps)
print(x)
print(steps)
for i in range(len(x)):
    print(x[i] - acc[i])
print("\n Seidel:")
x, steps = Iter.Seidel(matrix, b, eps)
print(x)
print(steps)

for i in range(len(x)):
    print(x[i] - acc[i])