import data
import Newton
import time
import numpy as np
import matplotlib.pyplot as plt

elpL = []
def test(k, kmax=1e3):
    print("\n Test k = " + str(k) + ", kmax = " + str(kmax))
    time0 = time.time()
    newton, num = Newton.Newton(funcSystem, x0, k, kmax=kmax)
    time1 = time.time()
    print("Newton: ")
    print(newton)
    print("Number of iterations: ")
    print(num)
    print("Elapsed time: ")
    elp = time1 - time0
    elpL.append(elp)
    print(elp)
    print()
funcSystem = data.getFuncSystem()
x0 = data.getStartVector()
'''
print("x0: ")
print(x0)

testMax = 25
for i in range(1,testMax):
    test(i)
iL = np.arange(1,testMax)
plt.plot(iL, elpL)
plt.show()
test(-1)
'''
x0[4] = -0.2
print("x0: ")
print(x0)
test(1)
test(5)
test(8)
test(10)
test(1,3)
test(1,5)
test(1,10)
test(1,20)