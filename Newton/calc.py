import data
import Newton
import time

def test(k):
    print("\n Test k = " + str(k))
    time0 = time.time()
    newton, num = Newton.Newton(funcSystem, x0, k)
    time1 = time.time()
    print("Newton: ")
    print(newton)
    print("Number of iterations: ")
    print(num)
    print("Elapsed time: ")
    print(time1 - time0)
    print()
funcSystem = data.getFuncSystem()
x0 = data.getStartVector()
print("x0: ")
print(x0)
test(1)
test(3)
test(10)
test(20)
test(30)
test(50)
test(-1)
x0[4] = -0.2
print("x0: ")
print(x0)
test(5)
test(8)
test(10)