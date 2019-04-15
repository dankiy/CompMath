import LU
import Generate

matrix, b = Generate.Generate(5)
luMatrix = LU.LU(matrix, b)
print("show: ")
luMatrix.show()
print("solve: ")
print(luMatrix.solve())
print("det: ")
print(luMatrix.det())

