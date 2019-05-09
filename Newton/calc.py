import data
import Newton
import time

funcSystem = data.getFuncSystem()
x0 = data.getStartVector()
print("x0: ")
print(x0)
time0 = time.time()
newton, num = Newton.Newton(funcSystem, x0)
time = time.time()
print("Newton: ")
print(newton)
print("Number of iterations: ")
print(num)
print("Elapsed time: ")
print(time - time0)