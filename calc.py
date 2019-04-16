import LU
import Generate
import numpy as np

#matrix, b = Generate.Generate(5)
matrix = np.ones(5,5)
b = np.array([1,2,3,4,5], dtype=float)
print("matrix:")
print(matrix)
print("b:")
print(b)
luMatrix = LU.LU(matrix, b)
print("show: ")
luMatrix.show()
print("solve: ")
print(luMatrix.solve())
print("det: ")
print(luMatrix.det())
print("L*U:")
print(np.multiply(np.tril(luMatrix.C,-1)+np.eye(len(luMatrix.C)), np.triu(luMatrix.C)))
print("P*A:")
print(np.multiply(luMatrix.P, matrix))

