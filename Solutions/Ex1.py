def function(x):
    y = x - 2**(0.33)
    return y

def newtonian_function(x):
    for n in range(3):
        x -= function(x)
    return x

root = 1.259921
approximation = round(newtonian_function(2), 6)

error_perchentage = (1 - approximation/root)*100)
