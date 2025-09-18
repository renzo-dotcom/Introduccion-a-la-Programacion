#Histograma

import random
ale=random.randint(1,9)

n=int(input("Ingrese el orden de la fila de la matriz"))
for x in range (n) :
    for y in range (5):
        print(x,end=" ")
    print()