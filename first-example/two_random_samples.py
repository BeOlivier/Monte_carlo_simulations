import numpy as np
import matplotlib.pyplot as plt

#? From: https://www.youtube.com/watch?v=slbZ-SLpIgg

#! First simulate random outcomes between two set ranges

sims = 1000000  # Number of simulations to run

A = np.random.uniform(1, 5, sims)
B = np.random.uniform(2, 6, sims)

duration = A + B
# print(duration)

plt.figure(figsize = (3, 1.5))
plt.hist(duration, density = True)
plt.axvline(9, color = 'r')
plt.show()
print((duration > 9).sum()/sims)