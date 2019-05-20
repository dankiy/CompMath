from Integral import NPI, CPI, ACPI
from scipy.integrate import quad
from math import cos, exp, sin

def f(x):
    return 3*cos(1.5*x)*exp(x/4) + 4*sin(3.5*x)*exp(-3*x) + 4*x
a = 2.5
b = 3.3

print(NPI(f, a, b))
print(CPI(f, a, b, steps=10))
print(ACPI(f, a, b, eps=1e-6, opt=False))
print(quad(f, a, b))
