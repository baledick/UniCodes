number=input("Give me a number, and I will find all numbers before it ")
n=int(number)
for j in range(2,n):
    p=0
    for i in range(2,j):
        if (j%i == 0):
            p=1
    if p==0:
        print(j, "is prime")

        
