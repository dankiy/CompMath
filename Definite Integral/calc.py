from Integral import NPI, GPI, CPI, ACPI
from scipy.integrate import quad
from math import cos, exp, sin

def f(x):
    return 2*cos(2.5*x)*exp(x/3) + 4*sin(3.5*x)*exp(-3*x) + x
a = 1.5
b = 3.3
eps = 1e-9

print("NPI: ")
print(NPI(f, a, b))
print("GPI: ")
print(GPI(f, a, b))
print("CPI Newton: ")
print(CPI(f, a, b, steps=10))
print("ACPI Newton, eps = " + str(eps) + ": ")
print(ACPI(f, a, b, eps=eps, opt=False))
print("ACPI Newton, eps = " + str(eps) + ", hopt = True: ")
print(ACPI(f, a, b, eps=eps, opt=True))
print("CPI Gauss: ")
print(CPI(f, a, b, steps=10, gauss=True))
print("ACPI Gauss, eps = " + str(eps) + " : ")
print(ACPI(f, a, b, eps=eps, opt=False, gauss=True))
print("ACPI Gauss, eps = " + str(eps) + ", hopt = True: ")
print(ACPI(f, a, b, eps=eps, opt=True, gauss=True))
print("scipy.integrate.quad: ")
print(quad(f, a, b))
