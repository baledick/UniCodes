import numpy as np

def function(x, y, z):
    value = x/((y**2+ z**2 -2*xyz)**0.5)
    return value

a = -1
b = 1
n = 20
h = (b-a)/n
s = function(a)+function(b)
for i in range(n):
    if i%2 == 0 :
        s += 4*function((a+i)*h)
    else:
        s += 2*function((a+i)*h)


##WIP
