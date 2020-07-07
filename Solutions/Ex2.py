import numpy as np

def integral(x):
    y = x**2
    return y

n0 = 0 # this is the integral
n1 = 0 # this is the deviation
a=1
b=11

array = [5, 9, 4]
for i in range(3):
    rand = array[i]
    n0 += integral(rand)
    n1 += integral(rand)**2

int = (b-a)*n0/3
sigma = ((n1/3) - ((n0/3)**2))**0.5
dI = sigma/(3**0.5)
print(int, "+/-", dI)
