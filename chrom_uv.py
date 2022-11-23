import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import math
import random

#Generating a chromatogram using the gaussian equation with parameters, mu and sigma


retentionTime = [3.6, 2.46, 1.30, 4.22, 6.5]
width = []
N = 3000 #Column efficiency

for mu in retentionTime:
    width.append(4 * mu / math.sqrt(N))

sigma = []
for w in width:
    sigma.append(w / 4)



#the X-axis as the retentiontime

x_data = np.arange(0, 10, 0.001)

# H is the automatically generated peak height from the gaussian equation
# x,mu and s represent x-axis,retention time and peak width respectively


def peak(x, mu, s):
    H = 1 / math.sqrt(2 * math.pi * s**2) # H is the automatically generated peak height from the gaussian function which can be manipulated
    return H * np.exp(-0.5 / s**2 * (x - mu)**2) # gaussian output

 


y_data = peak(x_data, retentionTime[0], sigma[0]) + peak(x_data, retentionTime[1], sigma[1]) + peak(x_data, retentionTime[2], sigma[2])


plt.plot(x_data, y_data)
plt.xlabel("Retention Time(min)")
plt.ylabel("Peak Height")
plt.title("Chromatogram using UV detector")


plt.show()

