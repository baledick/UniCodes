import numpy as np
import matplotlib.pyplot as plt

def decayrate(): #the decay rate function
    dead = False
    tau = np.random.uniform(0,1)
    if tau  < ell :
        dead = True
    return dead

ell = 0.001
N=10000
nc= []
time = []
u=0

while(N>0):
    for i in range(N):
        if decayrate():
            N=N-1
       #     print(len(nc))
    nc +=[N]
    time += [u]
    u += 1

plt.plot(time, nc)
plt.show()
