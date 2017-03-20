import matplotlib.pyplot as plt
import numpy as np
import math
import os
import sys

hbar = 1.0
a = 1.0
pi = math.pi
m = 3.0
G = 2*pi/a
U = 2.0

k = np.arange(-3*pi/a, 3*pi/a, 0.01) 
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)

ek = (hbar**2)*(k**2)/(2*m)
ekG = (hbar**2)*((k - G)**2)/(2*m)
ekGP = (hbar**2)*((k + G)**2)/(2*m)
e1 = ((ekGP + ekG)/2) + np.sqrt((ekGP - ekG)**2/4 + U**2)
e2 = ((ekGP + ekG)/2) - np.sqrt((ekGP - ekG)**2/4 + U**2)
e3 = ((ek + ekG)/2) + np.sqrt(((ek - ekG)/2)**2 + U**2)
e4 = ((ek + ekG)/2) - np.sqrt(((ek - ekG)/2)**2 + U**2)
e5 = ((ek + ekGP)/2) + np.sqrt(((ek - ekGP)/2)**2 + U**2)
e6 = ((ek + ekGP)/2) - np.sqrt(((ek - ekGP)/2)**2 + U**2)
ax.plot(k, e1, label="$E_+ (k = 0)$", linewidth=2.0)
ax.plot(k, e2, label="$E_- (k = 0)$", linewidth=2.0)
ax.plot(k, k*k + 8.6, linestyle='dashed', color="blue", linewidth=2.0)
ax.plot(k, -k*k + 4.51, linestyle="dashed", color="green", linewidth=2.0)

ax.set_xlim(-pi/a,pi/a)
ax.set_ylim(0,15)
ax.tick_params(axis='x', labelsize=18)
ax.set_xlabel("\\textbf{k}", fontsize=20)
ax.yaxis.set_major_formatter(plt.NullFormatter())
plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif')
plt.tight_layout()
plt.savefig("parabolic_quantized.png")
#plt.show()