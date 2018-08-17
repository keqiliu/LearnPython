import numpy as np
from scipy import linalg
from scipy import integrate
from scipy import stats
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import sympy as sy

# ndarray
"""
1. array store the SAME type
2. take less memory than lists
"""

# same type
print(np.array([2, 3, 5]))  # all int
print(np.array([2, 3, 5.]))  # all float
print(np.array([2, 3, 5+1j]))  # all complex

# generate
print(np.arange(2, 12, 3))
print(np.linspace(2, 12, 3))  # used to generate plot!
print(np.zeros((2, 1), complex))
print(np.ones(5))
print(np.ndim(np.ones(5)))  # --> [5,] is 1 dimension vector!!


# it's all about shape shape!!!
a = np.array([[1, 2, 0], [3, 4, 5]])
print(a.shape)  # row, col
print(a.ndim)  # total dimension
print(a.size)   # total # of elements

b = a.reshape(1, 6)
print(b)

c = a.reshape(-1, 2)  # -1 means AUTO determine,
# if the other value is not factor, value error!!
print(c)

a = np.arange(1, 4)
print(a.shape)  # (3,) --> dimension = 1 !!!!
print(a.ndim)
b = a.copy()

print(np.dot(np.transpose(a), b))
print(np.dot(np.transpose(b), a))  # dot on 2 1-D arrays --> inner product of vectors!

ax = np.reshape(a, (3, 1))
bx = np.reshape(b, (1, 3))
print(np.dot(ax, bx))  # dot on 2 2-D matrix --> matrix multi! 3 * 3!!!

# * v.s. dot
a = np.reshape(np.arange(1, 5), (2, 2))
print(a * a)  # element-wise
print(np.dot(a, a))  # real

# random number
print(np.random.rand(2, 1))  # uniform distribution [0,1]
print(np.random.randn(2, 3))  # normal distribution N(0,1)


# array slicing
a = np.arange(5)
print(a[:])
print(a[1:-1])
print(a[::-1])

a = np.arange(12)
a = a.reshape(-1, 4)
print(a.shape)
print(a)
print(a[1, -1])  # 2nd row, last column
print(a[1][-1])  # equivalent as above!!
print(a[:, 1])  # 2nd column
print(a[0])  # 1st row

b = a[2:, 2:]
b[0][0] = 100
print(a)  # be careful!!! slicing refers to the same memory

b = a[2:, 2:].copy()  # copy avoids changing original value!
print(b)
b[0][0] = 999
print(b)
print(a)

# save to files
np.savetxt('array_save.txt', a)
x = np.loadtxt('array_save.txt')
print("load txt:", x)

np.save('aya', a)  # save as .npy file
x = np.load('aya.npy')
print("load npy:", x)

# math in numpy is faster than basic Math, esp. for LARGE SCALE data
print(np.log(3))
print(np.sin(3.11))
print(np.exp(3.11))

# Lab 1: numpy
a = np.arange(1,21)
b = np.reshape(a, (4, 5))
c = np.reshape(a, (5, 4))
print("matrix multi:", np.dot(b, c))


def integral(func, a, b, step=10000):
    x = np.linspace(a, b, step)
    sum_integral = 0
    for i in range(1, x.size):
        sum_integral += func(x[i]) * (x[i] - x[i-1])
    return sum_integral


def this_func(x):
    return np.sin(x+1)/np.exp(x)*(x+1)/2


ans = integral(this_func, 0, 1)
print("integral:", ans)

# scipy integrate!!
value, error = integrate.quad(this_func, 0, 1)
print("scipy integrate value", value)
print("scipy integrate error", error)


# scipy linear algebra
A = np.random.rand(3, 3)
b = np.random.rand(3)
x = linalg.solve(A, b)  # solve A x = b
print(x)
eigen = linalg.eig(A)  # eigens
print(eigen)
det = linalg.det(A)  # determinant
print(det)
U, s, Vh = linalg.svd(A)  # singular value decomposition


# statistics in scipy
y = stats.norm.cdf(0.311) # norm CDF
print(y)


# data fitting
def func(x , a, b, c):
    return a * np.exp(-b*x)+c


xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.2 * np.random.normal(size=xdata.shape)

popt, pcov = optimize.curve_fit(func, xdata, ydata)  # fitting!
print(popt)
print(pcov)

fig = plt.figure(figsize=(12, 6))
sub1 = fig.add_subplot(121)
plt.plot(xdata, ydata, 'b*')
plt.plot(xdata, func(xdata, popt[0], popt[1], popt[2]), 'r-')
plt.title('$f(x)=ae^{-bx}+c$ curve fitting')
# plt.show()
sub1.grid(True)  # show grid

# matplotlib
sub2 = fig.add_subplot(122)
x = np.linspace(0, 10, 201)
plt.plot(x, x**0.3, 'g--', lw=2, label='$y=x^{0.3}$')
plt.plot(x, x-1, 'k-', label='$y=x-1$')
plt.plot(x, np.zeros_like(x)+3, lw=2.5, label='$y=3$')
plt.plot(4, 3, 'ro', lw=3)
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2, 11)
plt.title('Check check', fontsize=22)
sub2.set_title('Check again', fontsize=18)  # overwrite above title
sub2.set_xlim(-1, 11)
sub2.annotate('$\Delta$ this', xy=(4, 3), xytext=(5, 2),
              arrowprops=dict(headwidth=8, width=3, facecolor='cyan', shrink=0.05))

fig.show()

# 3D plot
x, y = np.mgrid[-10:10:100j, -10:10:100j]
z = np.sin(x) + x**2 * 0.05 + np.sin(y) + y**2 * 0.05
fig = plt.figure(figsize=(8, 6))
ax = plt.axes(projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cmap=cm.coolwarm,
                       cstride=1, linewidth=0)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('3D plot of $z=\sin(x)+0.05x^2+\sin(y)+0.05y^2$')
fig.show()

t = np.linspace(0, np.pi * 2, 100)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3 * t) - np.cos(4 * t)
plt.plot(x, y, 'blue')
plt.title("It\'s a heart!",fontsize=20)
plt.savefig("heart.png")
plt.savefig("heart.pdf")
# plt.show()


# sympy, symbol variable
x = sy.Symbol('x')
y = sy.Symbol('y')
a, b = sy.symbols('a b')
f = x**2 + y**2 - 2*x*y + 5  # create a new sybol
print(f)
g = x**2 + 2 * x**2 - 2*x + 2 - 1 # AUTO simplify!! cool
print(g)

# symbol solve
print(sy.solve(x**2 - 1))
print(sy.solve(x**3 + 0.5*x**2 - 1))
print(sy.solve(x**3 + y**2))  # express x as a function of y
# print(sy.solve(x**x + 2*x - 1))
# NotImplementedError: multiple generators [x, x**x]
# No algorithms are implemented to solve equation 2*x + x**x - 1

# symbol integration
f = sy.sin(x) + sy.exp(x)
print(sy.integrate(f, (x, a, b)))
print(sy.integrate(f, (x, 1, 2)))  # take 1 and 2 as symbol
print(sy.integrate(f, (x, 1.0, 2.0)))  # real calculation on 1 * 2

g = sy.exp(x) + x * sy.sin(y)  # g = g(x,y)
print(sy.integrate(g, (y, a, b)))  # integral on y

# symbol differentiation
f = sy.cos(x) + x**x
print(sy.diff(f, x))
print(sy.diff(g, y))  # diff on y only



