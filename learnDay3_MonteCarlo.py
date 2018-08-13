import numpy.random as npr
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

X = npr.standard_normal((5000))
Y = npr.normal(1, 1, (5000))
Z = npr.uniform(-3, 3, (5000))
W = npr.lognormal(0, 1, (5000))

plt.subplot(221)
plt.hist(X)
plt.subplot(222)
plt.hist(Y)
plt.subplot(223)
plt.hist(Z)
plt.subplot(224)
plt.hist(W)
plt.show()

# MC
I = 10000
Z = npr.standard_normal(I)
ST = 1000 * Z
V = np.mean(np.maximum(ST, 0))
SD = np.std(np.maximum(ST, 0))
print("mean={0:.2f},std={1:.2f}".format(V, SD))
