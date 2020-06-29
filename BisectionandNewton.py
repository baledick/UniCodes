import numpy as np
def f(x):
	return np.tan(x)-x/(1-x**2) 
def df(x):
	return (1/np.cos(x))*(1/np.cos(x))-(x*x+1)/((x*x-1)*(x*x-1))

#a erwtima 1)

def bisection(f,a,b,N):
	if f(a)*f(b) >=0:
		print("Can't do this chief")
		return None
	for n in range (1, N+1):
		a_n=a
		b_n=b
		c_n=(a_n + b_n)/2
		if f(a_n)*f(c_n) <0:
			a=a_n
			b=c_n
		elif f(b_n)*f(c_n) <0:
			a=c_n
			b=b_n
		elif f(c_n) == 0:
			print("I found it boss")
			return c_n
	return (a_n+b_n)/2
approx1 = bisection(f,2,4,15)
print(approx1)

def newt(f,df,x0,e,M): 
	xn = x0
	
	for n in range(0,M):
		xn = xn - f(xn)/df(xn)
		if abs(f(xn)) < e:
			print('Found solution after',n,'iterations.')
	return xn
	if df(xn) == 0:
		print('Zero derivative. No solution found.')
		return None
approx2 = newt(f,df,3.0,1e-30,6)
print(approx2)







