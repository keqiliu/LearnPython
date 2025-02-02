# compute y = a0 + a1*x + a2*x^2 + ... + an*x^n

"""
Thinking process:
an -> *x
x * a_n + a_n-1 --> *x
(x * a_n + a_n-1) * x + a_n-2 --> *x
"""

import numpy as np


def manual_Horner(a, x):
    y = a[-1]
    for i in range(len(a)-2, -1, -1):
        y = y*x + a[i]
    return y

a = [5, 3, 2, 2]
x = 27

print(f"coefficient is {a}\nx = {x}")
print(f"manual result = {manual_Horner(a,x)}")

print(f"numpy to validate = {np.polyval(list(reversed(a)), x)}")