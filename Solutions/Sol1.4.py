import numpy as np
import matplotlib.pyplot as plt

def first(x, y):
    value = (20/13)*(x+y)
    return value
def second(x, y, z):
    value = (12/31)*(x**2 + y*z)
    return value
def rand(a, b):
    value = np.random.uniform(a, b)
    return value

n = 100000
n10 = 0
n11 = 0
n20 = 0
n21 = 0

for i in range(n):
    randx1 = rand(0,1)
    randy1 = rand(0,1)
    randx2 = rand(0,1)
    randy2 = rand(1,2)
    randz2 = rand(1,2)
    if randx1**2 <= randy1:
        n10 += first(randx1, randy1)
        n11 += first(randx1, randy1)**2
    n20 += second(randx2, randy2, randz2)
    n21 += second(randx2, randy2, randz2)**2

int1 = n10/n
sigma1 = ((n11/n) - ((n10/n)**2))**0.5
dI1 = sigma1/(n**0.5)
int2 = n20/n
sigma2 = ((n21/n) - ((n20/n)**2))**0.5
dI2 = sigma2/(n**0.5)

print(int1, "+/-", dI1)
print(int2, "+/-", dI2)
