import numpy as np
import matplotlib.pyplot as plt

def function(x):
    y = np.tan(x) - x/(1-x**2)
    return y

def derivative(x):
    y = (1/np.cos(x))**2 - ((x**2 + 1)/((x**2 - 1)**2))
    return y

#Prwto erwtima
#a)
def bisection_function(a,b):
    for n in range(16):
        c = (a + b)/2
        if function(a)*function(c) < 0:
            b = (a + b)/2
        else:
            a = (a + b)/2
    return c

bisection_function(2,4)
#b)
def newtonian_function(x):
    for n in range(6):
        x -= (function(x)/derivative(x))
    return x

newtonian_function(3)
#Telos prwtou erwtimatos

#Deutero erwtima
for i in range(4,10):
    root = newtonian_function(i)
    if (root > 4 and root!= previous_root):
        print(root)
    else:
        continue
    previous_root = root
#Telos deuterou erwtimatos
