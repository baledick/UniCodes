#erwtima a
e=1.0
while(1.0 + e != 1.0):
	e=0.5*e
print("e = ",e)
input('Pata Enter gia na ypologisei tin paragwgo')
def f(x):
	return x*x
def der(func, x, j):
	return (func(x+(j))-func(x))/(j)
print("I paragwgos gia n = 1 einai ", der(f, 2, 1*e))
print("I paragwgos gia n = 2 einai ", der(f, 2, 2*e))
print("I paragwgos gia n = 3 einai ", der(f, 2, 3*e))
print("I paragwgos gia n = 4 einai ", der(f, 2, 4*e))
print("I paragwgos gia n = 5 einai ", der(f, 2, 5*e))
print("I paragwgos gia n = 50000 einai ", der(f, 2, 50000*e))
print("I paragwgos gia n = 50001 einai ", der(f, 2, 50001*e))
print("I paragwgos gia n = 50002 einai ", der(f, 2, 50002*e))
print("I paragwgos gia n = 50003 einai ", der(f, 2, 50003*e))
#erwtima b
print("\nSto erwtima b twra \n")
def g(x , y):
	return x/y
print("To prwto klasma einai", g(0.1+0.1-0.2, e))
print("To deutero klasma einai", g(0.1+0.2-0.3, e))
i=(7.0/3.0)
j=(4.0/3.0)
k=(3.0/3.0)
print("To trito klasma einai ", g(i-j-k, e))

input('Press Enter to end the program...')



