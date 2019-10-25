#Matrix operations
import numpy as np
	z = np.zeros((9,1))
	A = np.array([[4,-1,0,-1,0,0,0,0,0],
	             [-1,4,-1,0,-1,0,0,0,0],
	             [0,-1,4,0,0,-1,0,0,0],
	             [-1,0,0,4,-1,0,-1,0,0],
	             [0,-1,0,-1,4,-1,0,-1,0],
	             [0,0,-1,0,-1,4,0,0,-1],
	             [0,0,0,-1,0,0,4,-1,0],
	             [0,0,0,0,-1,0,-1,4,-1],
	             [0,0,0,0,0,-1,0,-1,4]])
	b = np.array([[4],[-1],[-5],[-2],[2],[2],[-1],[1],[6]])
	a = np.linalg.inv(A) # antistrofos tou A
	x = np.dot(a,b)# Ax=b => x=ab
	print(x)
	Ax=np.dot(A,x)
	C=np.subtract(Ax,b)
	np.array_equal(C,z)
