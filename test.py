import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
import math
import random


#Chromatographic data in a Dataframe.Data generated
df = pd.DataFrame({
    "Peak": ['1', '2', '3', '4', '5'],
    "Retention Time": ['2.39', '2.46', '1.30', '4.22', '6.5'],
    "Width @ Base": ['0.102', '0.119', '0.127', '0.144', '0.280']
})

print(df)

#A software to generate a single chromatogram peak using the above data for Peak 1


#width = 4 times the standard deviation sigma

retentionTime = [3.6, 2.46, 1.30, 4.22, 6.5]
width = []
N = 3000

for mu in retentionTime:
    width.append(4 * mu / math.sqrt(N))

sigma = []
for w in width:
    sigma.append(w / 4)

#x-axis as the period of retention time  
x_data = np.arange(0, 7, 0.001)


noise = np.random.normal(0, 1, len(x_data))
# Noise up the original signal

for sig,mu in zip(sigma, retentionTime):
    
    ## y-axis as the gaussian for 4 peaks
    y_data = stats.norm.pdf(x_data, retentionTime[0], sigma[0]) + stats.norm.pdf(x_data, retentionTime[1], sigma[1])  + stats.norm.pdf(x_data, retentionTime[2], sigma[2]) + stats.norm.pdf(x_data, retentionTime[3], sigma[3]) + stats.norm.pdf(x_data, retentionTime[4], sigma[4]) + noise
    


plt.xlabel("Retention Time(min)")
plt.ylabel("Peak Height")
plt.title("Chromatogram")


plt.plot(x_data, y_data)

plt.show()
