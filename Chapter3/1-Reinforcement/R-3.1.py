# Graph the functions 8n, 4nlogn, 2n^2, n^3, and 2^n using a logarithmic scale
#  for the x- and y-axes; that is, if the function value f(n) is y, plot this as a
#  point with x-coordinate at logn and y-coordinate at logy.
import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(0, np.log(5), 100)
y1 = 8 * x
y2 = 4 * x * np.log(x)
y3 = 2 * x ** 2
y4 = x ** 3
y5 = 2 ** x

plt.figure()
plt.plot(x, y1, label='8n')
plt.plot(x, y2, label='4n log n')
plt.plot(x, y3, label='2n²')
plt.plot(x, y4, label='n³')
plt.plot(x, y5, label='2ⁿ')

plt.legend()
plt.grid(True,  which='both', linestyle='--', alpha=0.5)
plt.xscale('log')
plt.yscale('log')
plt.show()
