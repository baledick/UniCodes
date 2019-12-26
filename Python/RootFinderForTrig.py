import numpy as np

def f(x):
	return np.tan(x)-x/(1-x**2)
def df(x):
	return (1/np.cos(x))*(1/np.cos(x))-(x*x+1)/((x*x-1)*(x*x-1))
def ddf(x):
	return -x*((8*x**2)/(1 - x**2)**3 + 2/(1 - x**2)**2)-(4*x)/(1-x**2)**2 + 2*np.tan(x)*(1/np.cos(x))*(1/np.cos(x))
def checker(ddf, a, b, N, e):
	while (ddf(b)*ddf(b+e)<0 and ddf(b)*ddf(b+e)<0):
		if ddf(a)*ddf(a+e)>=0:
			if ddf(b)*ddf(b+e)>=0:
				print("No root in ["b,b+e,"]")
				b=b+e
				return None
			elif ddf(b)*ddf(b+e)<0:
				print("Found root for b")
				return b
			print("No root in ["a,a+e,"]")
			a=a+e
			return None
		elif ddf(a)*ddf(a+e)<0:
			if ddf(b)*ddf(b+e)>=0:
				print("No root in ["b,b+e,"]")
				b=b+e
				return None
			elif ddf(b)*ddf(b+e)<0:
				print("Found root for b")
				return b
			print("Here")
			return a
	return a,b
approx = checker(f,df,3.0,1e-30,6)
print(approx)
