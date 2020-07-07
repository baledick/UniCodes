import numpy as np

def integral(x):
    y = x**2
    return y

n = 100000
n0 = 0 # this is the integral
n1 = 0 # this is the deviation
a = 1
b = 11

for i in range(n):
    rand = np.random.uniform(a,b)
    n0 += integral(rand)
    n1 += integral(rand)**2

int = (b-a)*n0/n
sigma = ((n1/n) - ((n0/n)**2))**0.5
dI = sigma/(n**0.5)
print(int, "+/-", dI)
