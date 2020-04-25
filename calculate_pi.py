from decimal import Decimal, getcontext
from math import factorial
import timeit

getcontext().prec = 1000


def Leibniz(n):
    pi = Decimal(0)
    for i in range(n):
        nom = (-1) ** i
        denom = 2 * i + 1
        pi += Decimal(nom) / Decimal(denom)
    pi *= 4
    return round(pi, n)


def Chudnovsky(n):
    pi = Decimal(0)

    for k in range(n):
        t = ((-1) ** k) * (factorial(6 * k)) * (13591409 + 545140134 * k)
        deno = factorial(3 * k) * (factorial(k) ** 3) * (640320 ** (3 * k))
        pi += Decimal(t) / Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1 / pi
    return round(pi, n)


code_1 = """\

def Leibniz(n):
    pi = Decimal(0)
    for i in range(n):
        nom = (-1) ** i
        denom = 2 * i + 1
        pi += Decimal(nom) / Decimal(denom)
    pi *= 4
    return round(pi, n)
"""

code_2 = """\

def Chudnovsky(n):
    pi = Decimal(0)
    for k in range(n):
        t = ((-1) ** k) * (factorial(6 * k)) * (13591409 + 545140134 * k)
        deno = factorial(3 * k) * (factorial(k) ** 3) * (640320 ** (3 * k))
        pi += Decimal(t) / Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1 / pi
    return round(pi, n)
"""

terms = int(input('Give the number of pi digits: '))
print('\n')

print(f'Pi with Leibniz algorithm: {Leibniz(terms)}')
print('\n')
print(f'Pi with Chudnovsky algorithm: {Chudnovsky(terms)}')
print('\n')

elapsed_time_1 = timeit.timeit(code_1, number=100) / 100

elapsed_time_2 = timeit.timeit(code_2, number=100) / 100

print(f'Leibniz algorithm took {elapsed_time_1} seconds to complete while Chudnovsky algorithm took {elapsed_time_2}'
      f' seconds to complete ')
