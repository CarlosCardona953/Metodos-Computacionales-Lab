import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.stats import f
from scipy.stats import norm

data = np.loadtxt(sys.argv[1])


R_viejo = data[:,0]
F_viejo = data[:,1]
R_nuevo = data[:,2]
F_nuevo = data[:,3]
b=60

plt.figure(figsize=(15,10))
plt.subplot(2,2,1)

plt.hist(R_viejo, bins=b, alpha=1, edgecolor = 'black', linewidth=1)
plt.title("$R^2$")


plt.subplot(2,2,2)
plt.hist(F_viejo, bins=b, alpha=1, edgecolor = 'black', linewidth=1)
plt.title("$F$")


plt.subplot(2,2,3)
plt.hist(R_nuevo, bins=b, alpha=1, edgecolor = 'black', linewidth=1)
plt.title("$Rnew^2$")


plt.subplot(2,2,4)
plt.hist(F_nuevo, bins=b, alpha=1, edgecolor = 'black', linewidth=1)
plt.title("$Fnew$")


plt.savefig("Ejercicio9_CarlosCardona.png")