import numpy as np
import matplotlib.pyplot as plt

def decayrate(): #the decay rate function
    dead = False
    tau = np.random.uniform(0,1)
    if tau  < ell :
        dead = True
    return dead

ell = 0.01
N=100
nc= []

while(N>0):
    for i in range(N):
        if decayrate():
            N=N-1
            print(len(nc))
        nc+=[N]

plt.plot(np.arange(0,len(nc),1),nc)
plt.show()
