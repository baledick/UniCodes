import numpy as np

A = [[2, 2, 3], [-1, -3, 0], [1,2,1]]
b = [3, 2, 0]
e = 3
x = np.zeros(e)
for i in range(e): #Gauss-Jacobi
    m = x[0]
    n = x[1]
    p = x[2]
    x[0] = (3-2*n-3*p)/2
    x[1] = -(2 + m)/3
    x[2] = -(m+ 2*n)
print(x)

x = np.zeros(e)
for i in range(e): #Gauss-Seidel
    x[0] = (3-2*x[1]-3*x[2])/2
    x[1] = -(2 + x[0])/3
    x[2] = -(x[0]+ 2*x[1])
print(x)
