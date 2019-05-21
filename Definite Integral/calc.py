from Integral import NPI, GPI, CPI, ACPI
from scipy.integrate import quad
from math import cos, exp, sin

def f(x):
    return 2*cos(2.5*x)*exp(x/3) + 4*sin(3.5*x)*exp(-3*x) + x
a = 1.5
b = 3.3

print(NPI(f, a, b))
print(GPI(f, a, b))
print(CPI(f, a, b, steps=10))
print(ACPI(f, a, b, eps=1e-14, opt=False))
print(quad(f, a, b))
