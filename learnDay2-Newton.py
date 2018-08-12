# Target 2
"""
y = x ^ (x/3)
"""

import numpy as np
import scipy.optimize as opt


def func_d(func, x, bump=0.01):
    y_up = func(x + bump)
    y_down = func(x - bump)
    return (y_up - y_down) / 2 / bump


def newton_solve(func, y0, x0):
    def func_zero(a):
        return func(a) - y0
    x = x0
    while abs(func_zero(x)) > 1e-15:
        x = x - func_zero(x)/func_d(func_zero, x)
    return x


def bisection_solve(func, y0, a, b):
    def func_zero(x):
        return func(x) - y0
    a_sign = np.sign(func_zero(a))
    b_sign = np.sign(func_zero(b))
    if a_sign == b_sign:
        raise Exception('Input a, b must yield to different sign')
    c = (a + b) / 2
    y_c = func_zero(c)
    while abs(y_c) > 1e-15:
        if np.sign(y_c) == b_sign:
            b = c
            b_sign = np.sign(func_zero(b))
        else:
            a = c
        c = (a + b) / 2
        y_c = func_zero(c)
    return c


def this_func(x):
    return x ** (x / 3)


x1 = bisection_solve(this_func, 2, 1, 3)
print("bisection: x1={0:.4f}".format(x1))
print(x1, '\n')

x2 = opt.bisect(lambda x: this_func(x)-2, 1, 3)
print("scipy bisec: x2={0}\n".format(x2))

x3 = newton_solve(this_func, 2, 1)
print("Newton: x3={0}\n".format(x3))

x4 = opt.newton(lambda x: this_func(x)-2, 1)
print("scipy newton: x4={0}\n".format(x4))
