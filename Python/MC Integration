import numpy as np
import math

def Density1(x,y):
    return (20/13)*(x+y)
def Density2(x,y,z):
    return (12/31)*(x+(y*z))
def U(a,b):
    return np.random.uniform(a,b)
def Sq(x):
    return x*x
n=1000
sum1=0
sum1sq=0
sum2=0
sum2sq=0

n=1000
sum1=0
sum1sq=0
sum2=0
sum2sq=0

for i in range(n):
    X=U(0,1)
    Y=U(0,1)
    if Sq(X)<=Y:
        sum1+=Density1(X,Y)
        sum1sq+=Density1(X,Y)**2

for i in range(n):
    A=U(0,1)
    B=U(1,2)
    C=U(1,2)
    sum2+=Density2(A,B,C)
    sum2sq+=Density2(A,B,C)**2



mean1=sum1/n 
sig1sq=(sum1sq/n)-((n-1)*(mean1*mean1)/n)
sig1=sig1sq**0.5
V1=1
I1=V1*mean1
dI1=V1*sig1/(n**0.5)

mean2=sum2/n
sig2sq=(sum2sq/n)-((n-1)*(mean2*mean2)/n)
sig2=sig2sq**0.5
V2=1
I2=V2*mean2
dI2=V2*sig2/(n**0.5)

print("The first integral is ", I1, "+/-", dI1)
print("The second one is", I2, "+/-", dI2)
