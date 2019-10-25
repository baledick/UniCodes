import numpy as np

def f(x):
	return np.tan(x)-x/(1-x**2) #orizw tin sinartisi
def df(x):
	return (1/np.cos(x))*(1/np.cos(x))-(x*x+1)/((x*x-1)*(x*x-1))
def ddf(x):
	return -x*((8*x**2)/(1 - x**2)**3 + 2/(1 - x**2)**2)-(4*x)/(1-x**2)**2 + 2*np.tan(x)*(1/np.cos(x))*(1/np.cos(x))
def checker(ddf, a, b, N, e):
	while (ddf(b)*ddf(b+e)<0 and ddf(b)*ddf(b+e)<0):
		if ddf(a)*ddf(a+e)>=0:
			if ddf(b)*ddf(b+e)>=0:
				print("Den exei riza sto ["b,b+e,"]")
				b=b+e
				return None
			elif ddf(b)*ddf(b+e)<0:
				print("vrika riza gia to b")
				return b
			print("Den exei riza sto ["a,a+e,"]")
			a=a+e
			return None
		elif ddf(a)*ddf(a+e)<0:
			if ddf(b)*ddf(b+e)>=0:
				print("Den exei riza sto ["b,b+e,"]")
				b=b+e
				return None
			elif ddf(b)*ddf(b+e)<0:
				print("vrika riza gia to b")
				return b
			print("Edw eimaste")
			return a
	return a,b
approx = checker(f,df,3.0,1e-30,6)
print(approx)
