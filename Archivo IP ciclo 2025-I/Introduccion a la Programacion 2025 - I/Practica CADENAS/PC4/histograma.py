import random

flag=True
n=int(input("Ingrese el orden de la matriz: "))

while (flag):
    if n%2!=0:
        n=int(input("Debe ingresar un orden par: "))
    else: 
        flag=False

for x in range(n):
    ale=random.randint(1,9)
    print(ale,end=" ")
    for y in range(ale):
        print("x",end=" ")
    print()