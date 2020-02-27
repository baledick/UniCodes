#eisagagw vivliothikes
import math
import numpy as np
import matplotlib.pyplot as plt

#orizw sinartiseis
def Mu(x,y):
    return 10*math.log10((1-x*x*T*T)*(1-x*x*T*T)+(2*x*y*T)*(2*x*y*T))
def Phi(x,y):
    return math.atan((2*x*y*T)/(1-x*x*T*T))
def Omega(x):
    return math.pow(10,x)

#kanw vectors tis sinartiseis pali
M= np.vectorize(Mu)
P= np.vectorize(Phi)
W= np.vectorize(Omega)
#
T=1
#auta einai ta diastimata, to w einai o sindiasmos twn w1,w2
w1=np.arange(0.1,1,0.1)
w2=np.arange(1.1,3.1,0.5)
w=np.hstack((w1,w2))
z=np.array([0.1, 0.4, 1])

#vriskw tis times san listes
valM1=M(W(w),z[0])
valM2=M(W(w),z[1])
valM3=M(W(w),z[2])

valP1=P(W(w),z[0])
valP2=P(W(w),z[1])
valP3=P(W(w),z[2])

#ta grafimata vgazoun lathos sxima, den exw idea pws tha eprepe na fainete
plt.plot(w, valM1, 'r')
plt.plot(w, valM2, 'g')
plt.plot(w, valM3, 'b')
plt.xlabel("$\log(\omega)$")
plt.ylabel("Platos Apokrisis")
plt.show()

plt.plot(w, valP1, 'r')
plt.plot(w, valP2, 'g')
plt.plot(w, valP3, 'b')
plt.ylabel("Orisma")
plt.xlabel("$\log(\omega)$")
plt.show()

#orizw tis "real values"
MatM=np.array([valM1, valM2, valM3])
MatPM=np.array([valP1, valP2, valP3])

omega=np.array([0.75, 1.25])
Wo=W(w)
rvalM1=M(W(omega),z[0])
rvalM2=M(W(omega),z[1])
rvalM3=M(W(omega),z[2])

rvalP1=P(W(omega),z[0])
rvalP2=P(W(omega),z[1])
rvalP3=P(W(omega),z[2])

#Orizw tin lagrangian pwstinlene
def Lag(x, y, z, k, m):
	return k*((z-x)/(z-y))+m*((x-y)/(z-y))

#Vriskw tis times mesw tis apo panw sinartisis
resM11=Lag(Omega(0.75), W(w[6]), W(w[7]), MatM[0][6], MatM[0][7])
resM21=Lag(Omega(0.75), W(w[6]), W(w[7]), MatM[1][6], MatM[1][7])
resM31=Lag(Omega(0.75), W(w[6]), W(w[7]), MatM[2][6], MatM[2][7])

resM12=Lag(Omega(1.25), W(w[8]), W(w[9]), MatM[0][8], MatM[0][9])
resM22=Lag(Omega(1.25), W(w[8]), W(w[9]), MatM[1][8], MatM[1][9])
resM32=Lag(Omega(1.25), W(w[8]), W(w[9]), MatM[2][8], MatM[2][9])

#kai ta sfalmata
error1=[(resM11-rvalM1[0]), (resM12-rvalM1[1])]
error2=[(resM21-rvalM2[0]), (resM22-rvalM2[1])]
error3=[(resM31-rvalM3[0]), (resM32-rvalM3[1])]
print(error1, error2, error3)
