import numpy as np
import matplotlib.pyplot as plt

def intensity(x, y):
    value = 1/(1+(x**2)*(np.sin(y))**2)
    return value

def g(x):
    value = 2*x/((1-x)**2)
    return value

r=[0.7, 0.8, 0.9]

#a)
x = np.linspace(0, 2 * np.pi, 120)
for i in range(3):
    y = intensity(g(r[i]), x)
    plt.plot((x*180/np.pi), y)
    plt.xlabel("Degrees")
    plt.ylabel("Intensity")
plt.show()

#b)
x = np.linspace(0, 2 * np.pi, 15)
table=np.zeros(len(x))
for i in range(3):
    table = np.zeros(len(x))
    for j in range(len(x)):
        table[j] = intensity(g(r[i]), x[j])
    print("For r=", r[i], table)
