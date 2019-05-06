import data
import Newton

funcSystem = data.getFuncSystem()
print(funcSystem)
x0 = data.getStartVector()
print(x0)
newton, num = Newton.Newton(funcSystem, x0)
print(newton)
print(num)
