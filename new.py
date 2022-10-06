import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
from scipy import asarray as ar,exp
import math
import pylab


retentionTime = [3.6, 2.46, 1.30, 4.22, 6.5]
width = []
N = 3000 #Column efficiency

for mu in retentionTime:
    width.append(4 * mu / math.sqrt(N))

sigma = []
for w in width:
    sigma.append(w / 4)

# H represents sensitivity of peak height at a given wavelength
def model(position, width, H):
    return   (H / stats.norm.pdf(position,position,width)) * stats.norm.pdf(x_data, position, width)


x_data = np.arange(0, 10, 0.001)
y_1 =  model(retentionTime[0], sigma[0], 5)
y_2 =  model(retentionTime[0], sigma[0], 3) 
y_data = y_1 + y_2

plt.plot(x_data, y_1, x_data, y_2)
plt.show()