#eisagw tis vivliothikes mou
import math
import numpy as np
import matplotlib.pyplot as plt


#orizw tis sinartiseis
def Gamma(x):  
	return 4*x*x/((1-x*x)*(1-x*x))
def Iota(x, y):
	return 1/(1+x*x*math.sin(y)*math.sin(y))
def Delta(x):
	return math.pi*x/180

#metatrepw tis sinartieis se vector functions, wste na mporoun na dextoun lista timwn

G= np.vectorize(Gamma)
D= np.vectorize(Delta)
I= np.vectorize(Iota)

#ftiaxnw to diastima san lista timwn
d=np.arange(0, 384, 24)

#pairnw ta apotelesmata twn sinartisewn
val1=I(G(0.7),D(d))
val2=I(G(0.8),D(d))
val3=I(G(0.9),D(d))

#ftiaxnw to grafima
plt.plot(d, val1, 'r')
plt.plot(d, val2, 'g')
plt.plot(d, val3, 'b')
plt.xlabel("Gwnies(rad)")
plt.ylabel("Entasi")
plt.show()

#Edw ftiaxnw ena neo diastima kai pairnw tis "pragmatikes times"
delta=np.arange(90,360,90)

M=np.array([val1, val2, val3])

rval1=I(G(0.7),D(delta))
rval2=I(G(0.8),D(delta))
rval3=I(G(0.9),D(delta))

#kai twra pairnw ta apotelesmata

res11=Lag(Delta(90), d[3], d[4], d[5], M[0][3], M[0][4], M[0][5])
res21=Lag(Delta(90), d[3], d[4], d[5], M[1][3], M[1][4], M[1][5])
res31=Lag(Delta(90), d[3], d[4], d[5], M[2][3], M[2][4], M[2][5])

res12=Lag(Delta(180), d[7], d[8], d[9], M[0][7], M[0][8], M[0][9])
res22=Lag(Delta(180), d[7], d[8], d[9], M[1][7], M[1][8], M[1][9])
res32=Lag(Delta(180), d[7], d[8], d[9], M[2][7], M[2][8], M[2][9])

res13=Lag(Delta(270), d[11], d[12], d[13], M[0][11], M[0][12], M[0][13])
res23=Lag(Delta(270), d[11], d[12], d[13], M[1][11], M[1][12], M[1][13])
res33=Lag(Delta(270), d[11], d[12], d[13], M[2][11], M[2][12], M[2][13])

#paratirw oti ta sfalmata einai megista stin mesi blablabla auto exei na kanei me ton algorithmo tis Lag()
error1=[(res11-rval1[0]), (res12-rval1[1]),(res13-rval1[2])]
error2=[(res21-rval2[0]), (res22-rval2[1]),(res23-rval2[2])]
error3=[(res31-rval3[0]), (res32-rval3[1]),(res33-rval3[2])]

print(error1, error2, error3)
