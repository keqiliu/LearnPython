"""
Day 1
https://mp.weixin.qq.com/s?__biz=MzIxMjM4MjkwMw==&mid=2247483789&idx=1&sn=4c8fd2e76970a5d86c7b7a13c3046a30#rd
Day 2
https://mp.weixin.qq.com/s?__biz=MzIxMjM4MjkwMw==&mid=2247483920&idx=1&sn=96b11616cf48c83f54ac76c6687a20af#rd
Day 3
https://mp.weixin.qq.com/s?__biz=MzIxMjM4MjkwMw==&mid=2247483970&idx=1&sn=8028f7582597e0023f0fa02f84db57f1#rd
"""

import timeit
import numpy as np
from scipy import linalg
from scipy import integrate
from scipy import stats
from scipy.optimize import curve_fit
from scipy import optimize
import matplotlib.pyplot as plt
import matplotlib
import sympy as sy
import pandas as pd
matplotlib.use('TkAgg')

# -----------------------Day 1-----------------------------
# type: complex
c = 1+2j
print(type(c))
print(type(10/2))
print(type(10/3))

# type this in python console
# 0.1+0.2
# we will see
# 0.30000000000000004

round(9.99999, 6)

t = 'He is a string. Are you?'
print(t.split()) # default separated by " "
print(t.replace(' ', '|')) # does not change t
print(t.find('i'))
print(t.find('inn'))
print(t[0:4])

# The strip() method removes all leading and trailing characters that are in the provided string argument.
w = 'https://hswww.hoogle.com'
print(w.strip('https://')) # --> any char in this specified will be dropped from left or from right

a = [1, 'data']
print(type(a))
a.append([4, 3]) # only add 1 element!
print(a)
a.extend([4, 3]) # add all elements by "extend"
print(a)
a.insert(2, 'beta') # insert something onto index 2
print(a)
a.remove('data')
print(a)
a.remove('dataaaa') # --> error out when it's not in the list

x = [1, 2]
y = x # --> "=" will pass the value by ADDRESS!!!
y[0] = 5
print(x)

x = [1, 2]
z = x.copy()
z[0] = 5
print(x)

# create new file
file = open('newfile.txt', 'w')
file.write('ai ya. \n')
file.write('yo ho')
file.write('cool cool') # --> in the same line of last "yo ho" in txt
file.close()

# read
file = open('newfile.txt', 'r')
print(file.read()) # whole file
file = open('newfile.txt', 'r')
print(file.read(10)) # show first 10 chars
# continue from above line, read from 11th char
print(file.readline()) # show first 10 chars

# read by lines, readlines() read everything at once, takes more memory!!
file = open('newfile.txt', 'r')
for x in file.readlines():
    print(x)

# loop over file directly, pointer moves gradually line by line, small memory
# use this approach!!!!!!!!!!!!
file = open('newfile.txt', 'r')
for x in file:
    print(x)
file.close()

# adding new lines
file = open('newfile.txt', 'a')
file.write("\nI'm new line\n")
file.close()

# to avoid "forget to close the file"
with open('newfile.txt', 'a') as f:
    f.write('\n open again!!')

# -----------------------Day 2-----------------------------
# time it in fractional seconds
t_start = timeit.default_timer()
z = 109**2 + 357.1**11
t_end = timeit.default_timer()
print(t_end)
print(f'time cost is {t_end-t_start} seconds')

# homogeneous type in np.array
print(np.array([2, 3]))
print(np.array([2, 3, 4.0]))
print(np.array([2, 3, 4+1j]))

# create evenly spaced arrays
np.arange(5)
np.arange(10, 100, 30, dtype=float)

# start, stop, total number
# evenly split [start, stop] to "num" elements
np.linspace(0, 100, 4)
# array([0.,  33.33333333,  66.66666667, 100.])

# re-shape the array
a = np.arange(20)
print(a)
b = a.reshape((4, 5))
print(b)
c1 = a.reshape((20, 1)) # covert 1 dimension a into 2 dimension, vertical one
print(c1)
c2 = a.reshape((1, 20)) # covert 1 dimension a into 2 dimension, horizontal one
print(c2)
# a, c1, c2 are all different!!!!!!!!
d = a.reshape((-1, 2)) # -1 means shape is auto determined
print(d)
d = a.reshape((-1, 3)) # error out!! because 20 % 3 != 0

# np.dot on vector, dot product
a = np.arange(1, 6)
print(a)
b = a.copy()
# these two lines are the same
print(np.dot(np.transpose(a), b))
print(np.dot(a, np.transpose(b)))

# np.dot on matrix, matrix multiplication
aa = np.reshape(a, (5,1))
bb = np.reshape(b, (1,5))
# this is a 5x5 matrix!!
print(np.dot(aa, bb))

# np.dot, with scalar
print(np.dot(aa, 2))

# zero, ones, random numbers
print(np.zeros((3, 2), float))
print(np.ones((3, 2), int))
# rand() ~ U(0,1)
print(np.random.rand(3,2))
# randn() ~ N(0,1)
print(np.random.randn(3,2))

# slicing with steps
print(aa[:])
print(aa[::2])
print(aa[::-1]) # reverse


# 2D slicing
a = np.arange(20).reshape((4, 5))
print(a)
# 2nd column
print(a[:, 1])
# right bottom corner
print(a[2:, 3:])

# slicing on list creates copy
a = [1, 2, 3]
b = a[1:] # creates new copy
b[0] = 99
print(a, b) # a is NOT changed

# slicing on numpy refers to the same memory!!!
a = np.array([1, 2, 3])
b = a[1:] # creates new copy
b[0] = 99
print(a, b) # a is changed!!!!

# slicing on numpy refers to the same memory!!!
a = np.array([1, 2, 3])
b = a[1:].copy() # creates new copy
b[0] = 99
print(a, b) # a is NOT changed, after b uses copy

# * is element-wise operation
a = np.array([1, 2, 3, 4]).reshape((2,2))
print(a * a)
# matrix multiplication
print(np.dot(a, a))
b = [99, 2]
print(np.dot(a, b))

# save to files, and load
np.savetxt("np_save.txt", a)
np.save("np_save", a) # binary file

aaa = np.loadtxt("np_save.txt")
print(aaa)
print(type(aaa))

aaa = np.load("np_save.npy")
print(aaa)
print(type(aaa))

# it's all element-wise calculation
np.log(aaa)
np.sin(aaa)

# Linear Algebra
A = np.random.randn(5,5)
b = np.random.randn(5)
x = linalg.solve(A, b) # A x = b
print(x)
# eigen values
eigen = linalg.eig(A)
print(eigen) # array with eigen values, then eigen vectors
# determinant
det = linalg.det(A)
print(det)
# singular value decomposition
print(linalg.svd(A))

# Integral
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html
value, error = integrate.quad(np.log, 0, 1)
print(value)
print(error) # An estimate of the absolute error in the result.

# Statistics in scipy
print(stats.norm.cdf(1.2))
print(stats.norm.cdf(0))

# Curve Fit
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
def func (x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.2 * np.random.normal(size=len(xdata))
popt, pcov = curve_fit(func, xdata, ydata)
print(popt)
# To compute one standard deviation errors on the parameters, use
perr = np.sqrt(np.diag(pcov))
print(perr)

plt.plot(xdata, ydata, '*')
plt.plot(xdata, func(xdata, popt[0], popt[1], popt[2]), '-')
plt.title('$f(x)=ae^{-bx}+c$ curve fitting')

# optimization - root
def func(x):
    return np.exp(np.exp(x)) - x**2

# https://docs.scipy.org/doc/scipy-1.15.2/reference/generated/scipy.optimize.newton.html#scipy.optimize.newton
print(optimize.newton(func, 0)) #initial value = x
# https://docs.scipy.org/doc/scipy-1.15.2/reference/generated/scipy.optimize.bisect.html
print(optimize.bisect(func, -5, 5))

# Matplotlib
x= np.linspace(0, 11, 101)
plt.figure(figsize=(3, 3))
plt.plot(x, x**0.3, '--')
plt.plot(x, x-1, '-')
plt.plot(x, np.zeros_like(x)) # draw x-axis
plt.xlim(-2, 10)

# to annotate with LaTeX
plt.rcParams.update({
    "text.usetex": False,  # Disable full LaTeX (use built-in parser)
    "font.family": "serif",  # Use serif fonts for math symbols
})

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(121) # row, col, nums
# plot below will be in this defined subplot
plt.plot(x, x**0.3, '--')
plt.plot(x, x-1, '-')
ax.annotate(r'$\alpha\t\mathrm{and}\t\beta$',
            xy=(4,3),
            xytext=(6,3),
            arrowprops= dict(headwidth=3, width=0.5, facecolor='green',shrink=0.05))

# SymPy---  symbolic mathematics
# https://www.sympy.org/en/index.html
x = sy.Symbol('x')
y = sy.Symbol('y')
a, b = sy.symbols('a b')

f = x**2 + y**2 -2*x*y + 5
print(f)

print(sy.solve(x**2-1))
print(sy.solve(x**3 + y**2))

f= sy.sin(x) + sy.exp(x)
print(f)
print(sy.integrate(f, (x, a, b)))
print(sy.integrate(f, (x, 1, 2))) # a math formula
print(sy.integrate(f, (x, 1.0, 2.0))) # a float number after calculating


print(sy.diff(f, x))

g = sy.cos(y) * x + sy.log(y) * x**2
print(g)
print(sy.diff(g,y)) # PDE w.r.t. y