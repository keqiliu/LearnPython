import math

"""
Closed form (Binet's formula):
F(n) = [(1+sqrt(5))^n - (1-sqrt(5))^n] / (2^n * sqrt(5)]

Notes: A, B are roots for x^2 - x - 1 = 0, where A, B = (1 +/- sqrt(5))/2
Rewrite Binet's formula into:
F(n) = (A^n - B^n) / sqrt(5)

Induction:
if
F(n-1) * sqrt(5) = A^(n-1) - B^(n-1)
F(n) * sqrt(5) = A^n - B^n
then we need to prove:
F(n+1) * sqrt(5) = A^(n+1) - B^(n+1)

[F(n-1)+F(n)] * sqrt(5)
= A^(n-1) * (A+1) - B^(n-1) * (B+1)
= A^(n-1) * A^2 - B^(n-1) * B^2 // this is where we use the roots part
= A^(n+1) - B^(n+1)

All good!
"""

def fibonacci(n):
    x = list(range(n+1))
    x[0] = 0
    x[1] = 1
    for i in range(2, len(x)):
        x[i] = x[i-1] + x[i-2]
    return x[-1]


def binet_close_form(n):
    a = (1 + math.sqrt(5))/2
    b = (1 - math.sqrt(5))/2
    return (a**n - b**n)/math.sqrt(5)


# is that really close?
for power in range(10):
    n = 2**power
    print (f'n={n}\nfibonacci  ={fibonacci(n)}')
    print(f'close form ={binet_close_form(n):.2f}')


