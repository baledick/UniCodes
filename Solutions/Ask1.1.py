def epsilon():
    x = 1.
    while (1. + x != 1.):
        x = x/2
    return x

#Prwto erwtima

def square(x):
    y = x**2
    return y


n = np.array[(1, 2, 3, 4, 5, 50000, 50001, 50002, 50003)]

for number in n:
    dif = (square(2+(number*epsilon()))-square(2))/(number*epsilon())
    print(dif)
#Telos prwtou erwtimatos

#Deutero erwtima

def ratio():
    val = [[0.1, 0.1, -0.2], [0.1, 0.2, -0.3], [7/3, -4/3, -3/3]]
    for i in range(len(val)):
        x = 0
        for j in range(len(val[i])):
            x += val[i][j]
        y = x/epsilon()
        print(y)
    return None

ratio()
#Telos deuterou erwtimatos
