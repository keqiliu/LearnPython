"""
x ~ B(n,p)
for large n,
x ~ N(np, np(1-p) )
"""

import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

N = 1000

n, p = 10000, 0.2
y = np.random.binomial(n, p, N)
count, bins, ignored = plt.hist(y, 50, density=True)

mu = n * p
sigma = np.sqrt(n * p * (1-p))
plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
         linewidth=2, color='r')
plt.title("Binomial(n ={0}, p = {1})".format(n, p))
plt.show()


y2 = np.random.normal(mu, sigma, 1000)
count2, bins2, ignored2 = plt.hist(y2, 50, density=True)
plt.plot(bins2, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins2 - mu) ** 2 / (2 * sigma ** 2)),
         linewidth=2, color='r')
plt.title("Normal(np ={0}, np(1-p) = {1})".format(mu, sigma**2))
plt.show()

x2 = bernoulli.rvs(p, 0, N)
