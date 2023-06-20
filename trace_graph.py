#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

result = np.load('result.npy')
plt.plot(result[0], result[1], c='r')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.ylim(0, max(result[1])*1.25)
plt.show()
