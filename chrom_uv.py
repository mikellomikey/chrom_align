import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import math
import random

#Generating a chromatogram at different wavelengths 200nm and 250nm
#Lambda max for compound A is 250nm


retentionTime = [3.6]
width = []
N = 3000 #Column efficiency

for mu in retentionTime:
    width.append(4 * mu / math.sqrt(N))

sigma = []
for w in width:
    sigma.append(w / 4)

H = 0.4 / sigma[0]

#the X-axis as the retention time


# Generating clean data
x_data = np.arange(0, 10, 0.001)


 
#Set the required wavelength

     
y_2 = 0.05 * stats.norm.pdf(x_data, retentionTime[0], sigma[0])
y_3 = 0.8 * stats.norm.pdf(x_data, retentionTime[0], sigma[0])
y_4 = 0.4 * stats.norm.pdf(x_data, retentionTime[0], sigma[0])
y_5 = 0.23 * stats.norm.pdf(x_data, retentionTime[0], sigma[0])
y_6 = 0.36 * stats.norm.pdf(x_data, retentionTime[0], sigma[0])
y_7 = 0.5 * stats.norm.pdf(x_data, retentionTime[0], sigma[0])
y_8 = 0.15 * stats.norm.pdf(x_data, retentionTime[0], sigma[0])
y_9 = 0.67 * stats.norm.pdf(x_data, retentionTime[0], sigma[0])
y_10 = 0.74 * stats.norm.pdf(x_data, retentionTime[0], sigma[0])
    
y_data = stats.norm.pdf(x_data, retentionTime[0], sigma[0]) + y_2 + y_3 + y_4 + y_5 + y_6 + y_7 + y_8 + y_9 + y_10

plt.plot(x_data, y_data)

plt.xlabel("Retention Time(min)")
plt.ylabel("Peak Height")
plt.title("Chromatogram using UV detector")
plt.legend(['@ 250nm(lambda max)', '@ 200nm', '@ 239nm', '@ 240nm', '@ 269nm', '@ 215nm', '@ 224nm', '@ 235nm', '@ 266nm', '@270nm'])

plt.show()

plt.savefig('Outputs/chromatogram.jpeg')
    

